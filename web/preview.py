"""Write web/preview.html: the page wrapped in a full HTML document for local viewing.

Opened locally, the page runs in demo mode (template dialogue, formula scoring).
Claude-generated dialogue only works inside the published claude.ai page.
Usage: python3 web/preview.py, then open web/preview.html in a browser.
"""
from pathlib import Path

here = Path(__file__).parent
body = (here / "index.html").read_text(encoding="utf-8")
head = (
    '<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">'
    '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
    "<style>body{margin:0}[hidden]{display:none!important}</style></head><body>"
)
(here / "preview.html").write_text(head + body + "</body></html>", encoding="utf-8")
print("Wrote", here / "preview.html")
