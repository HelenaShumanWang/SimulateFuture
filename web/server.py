#!/usr/bin/env python3
"""Run Interview Room 2030 locally with DeepSeek writing the dialogue.

The page calls this server, and this server calls DeepSeek with your key.
The key stays on your computer: it is read from the DEEPSEEK_API_KEY
environment variable or from a .env file next to the repo's README, and it
is never sent to the browser.

Usage:
    python3 web/server.py            # then open http://127.0.0.1:8000
    python3 web/server.py --port 9000

Settings (environment variables or .env):
    DEEPSEEK_API_KEY     required for DeepSeek mode
    DEEPSEEK_MODEL       default: deepseek-chat
    DEEPSEEK_BASE_URL    default: https://api.deepseek.com
    DEEPSEEK_PRICE_IN    price per 1M input tokens shown in the page, default 0.28
    DEEPSEEK_PRICE_OUT   price per 1M output tokens shown in the page, default 0.42
    DEEPSEEK_CURRENCY    "$" or "¥", default "$"
    DEEPSEEK_MAX_SPEND   optional hard stop for this server process, in the same currency
"""
import argparse
import json
import os
import sys
import threading
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
USAGE_MARK = "\u0001"
MAX_PROMPT_CHARS = 60_000


def load_dotenv():
    for path in (ROOT / ".env", HERE / ".env"):
        if not path.exists():
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


load_dotenv()
KEY = os.environ.get("DEEPSEEK_API_KEY", "").strip()
MODEL = os.environ.get("DEEPSEEK_MODEL", "deepseek-chat").strip()
BASE_URL = os.environ.get("DEEPSEEK_BASE_URL", "https://api.deepseek.com").rstrip("/")
PRICE_IN = float(os.environ.get("DEEPSEEK_PRICE_IN", "0.28"))
PRICE_OUT = float(os.environ.get("DEEPSEEK_PRICE_OUT", "0.42"))
CURRENCY = "¥" if os.environ.get("DEEPSEEK_CURRENCY", "$").strip() == "¥" else "$"
MAX_SPEND = float(os.environ.get("DEEPSEEK_MAX_SPEND", "0") or 0)

spent = {"calls": 0, "in": 0, "out": 0, "cost": 0.0}
spent_lock = threading.Lock()


def add_spend(tokens_in, tokens_out):
    with spent_lock:
        spent["calls"] += 1
        spent["in"] += tokens_in
        spent["out"] += tokens_out
        spent["cost"] += (tokens_in * PRICE_IN + tokens_out * PRICE_OUT) / 1e6


def over_budget():
    return MAX_SPEND > 0 and spent["cost"] >= MAX_SPEND


def page_bytes():
    body = (HERE / "index.html").read_text(encoding="utf-8")
    head = (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        "<style>body{margin:0}[hidden]{display:none!important}</style></head><body>"
    )
    return (head + body + "</body></html>").encode("utf-8")


def upstream_error_message(err):
    try:
        data = json.loads(err.read().decode("utf-8", "replace"))
        return data.get("error", {}).get("message") or f"DeepSeek returned {err.code}"
    except Exception:
        return f"DeepSeek returned {err.code}"


class Handler(BaseHTTPRequestHandler):
    server_version = "InterviewRoom/1.0"

    def log_message(self, fmt, *args):
        # Log the request line only, never bodies or headers.
        sys.stderr.write(f"{self.command} {self.path.split('?')[0]}\n")

    def send_json(self, code, data):
        body = json.dumps(data).encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        path = self.path.split("?")[0]
        if path in ("/", "/index.html"):
            body = page_bytes()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)
        elif path == "/api/health":
            self.send_json(200, {
                "provider": "deepseek" if KEY else None,
                "model": MODEL if KEY else None,
                "price_in": PRICE_IN, "price_out": PRICE_OUT, "currency": CURRENCY,
            })
        elif path == "/api/usage":
            with spent_lock:
                self.send_json(200, dict(spent, currency=CURRENCY, max_spend=MAX_SPEND or None))
        else:
            self.send_json(404, {"error": "not found"})

    def do_POST(self):
        if self.path.split("?")[0] != "/api/chat":
            return self.send_json(404, {"error": "not found"})
        if not KEY:
            return self.send_json(503, {"error": "DEEPSEEK_API_KEY is not set on the server"})
        if over_budget():
            return self.send_json(402, {"error": f"Server spending cap of {CURRENCY}{MAX_SPEND} reached"})
        try:
            length = int(self.headers.get("Content-Length", "0"))
            req = json.loads(self.rfile.read(length) or b"{}")
        except Exception:
            return self.send_json(400, {"error": "bad request"})
        prompt = str(req.get("prompt", ""))
        if not prompt or len(prompt) > MAX_PROMPT_CHARS:
            return self.send_json(400, {"error": "prompt missing or too long"})
        stream = bool(req.get("stream"))
        try:
            temperature = max(0.0, min(1.5, float(req.get("temperature", 1.0))))
        except (TypeError, ValueError):
            temperature = 1.0
        payload = {
            "model": MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": temperature,
            "max_tokens": 2000,
            "stream": stream,
        }
        if stream:
            payload["stream_options"] = {"include_usage": True}
        if req.get("json"):
            payload["response_format"] = {"type": "json_object"}
        upstream = urllib.request.Request(
            BASE_URL + "/chat/completions",
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer " + KEY,
                "Accept": "text/event-stream" if stream else "application/json",
            },
        )
        try:
            resp = urllib.request.urlopen(upstream, timeout=180)
        except urllib.error.HTTPError as err:
            code = err.code if err.code in (400, 401, 402, 422, 429) else 502
            return self.send_json(code, {"error": upstream_error_message(err)})
        except Exception as err:
            return self.send_json(502, {"error": f"could not reach DeepSeek ({err.__class__.__name__})"})

        with resp:
            if not stream:
                data = json.loads(resp.read().decode("utf-8"))
                text = (data.get("choices") or [{}])[0].get("message", {}).get("content") or ""
                usage = data.get("usage") or {}
                tin, tout = int(usage.get("prompt_tokens", 0)), int(usage.get("completion_tokens", 0))
                est = not usage
                if est:
                    tin, tout = len(prompt) // 4, len(text) // 4
                add_spend(tin, tout)
                return self.send_json(200, {"text": text, "usage": {"in": tin, "out": tout, "est": est}})

            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            out_chars, usage = 0, None
            try:
                for raw in resp:
                    line = raw.decode("utf-8", "replace").strip()
                    if not line.startswith("data:"):
                        continue
                    chunk = line[5:].strip()
                    if chunk == "[DONE]":
                        break
                    try:
                        data = json.loads(chunk)
                    except ValueError:
                        continue
                    if data.get("usage"):
                        usage = data["usage"]
                    for choice in data.get("choices") or []:
                        delta = (choice.get("delta") or {}).get("content") or ""
                        if delta:
                            out_chars += len(delta)
                            self.wfile.write(delta.replace(USAGE_MARK, "").encode("utf-8"))
                            self.wfile.flush()
                est = not usage
                tin = int(usage.get("prompt_tokens", 0)) if usage else len(prompt) // 4
                tout = int(usage.get("completion_tokens", 0)) if usage else out_chars // 4
                add_spend(tin, tout)
                trailer = USAGE_MARK + json.dumps({"in": tin, "out": tout, "est": est})
                self.wfile.write(trailer.encode("utf-8"))
                self.wfile.flush()
            except (BrokenPipeError, ConnectionResetError):
                pass


def main():
    parser = argparse.ArgumentParser(description="Serve Interview Room 2030 with DeepSeek.")
    parser.add_argument("--host", default="127.0.0.1", help="default 127.0.0.1 (this computer only)")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()
    server = ThreadingHTTPServer((args.host, args.port), Handler)
    url = f"http://{'127.0.0.1' if args.host in ('0.0.0.0', '') else args.host}:{args.port}"
    print(f"Interview Room 2030 is running at {url}")
    if KEY:
        print(f"DeepSeek mode is on ({MODEL}). Your key stays on this computer.")
    else:
        print("No DEEPSEEK_API_KEY found, so the page will run in demo mode.")
        print("Add a line DEEPSEEK_API_KEY=sk-... to a .env file in the repo folder, then restart.")
    if args.host not in ("127.0.0.1", "localhost"):
        print("Warning: anyone who can reach this address can spend your DeepSeek balance.")
    if MAX_SPEND:
        print(f"This server stops calling DeepSeek after {CURRENCY}{MAX_SPEND} of estimated spend.")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")


if __name__ == "__main__":
    main()
