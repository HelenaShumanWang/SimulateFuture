# SimulateFuture: how people will deal with each other in the age of AI

We use generative agents, in the spirit of Stanford's "Smallville" town simulation, to explore how AI changes the way people interact: in university, in job interviews, and in the first year at work.

The goal is a **social wind tunnel, not a weather forecast**. We do not try to say "this is what 2030 will look like." We change one rule and watch the chain reactions between people.

**Try it:** [Interview Room 2030](https://claude.ai/artifact/9iyEj9ZfipFRNYMbEffmcc) is a pixel-art interview room where AI-played interviewers decide who gets the offer. To run it with DeepSeek on your own computer, see [Run the Interview Room](#3-run-the-interview-room).

---

## 1. What a simulation like this is good for

**What it cannot give you:** forecasts with numbers, such as "in 2030, X% of students will…". The model's knowledge comes from the past, and the results largely reflect the assumptions we write in.

**What it can give you:**

1. **Chain reactions you did not see coming.** After one rule changes, which way do trust, cooperation and competition move?
2. **A comparison between designs.** Under each design, who benefits, who loses, and what the side effects are.
3. **Explicit assumptions.** Every assumption lives in the configuration, where it can be questioned and changed one at a time.

**How to tell whether it means anything: check it against the real world first.** Either replay a period whose outcome we already know, or have real people make the same judgments and compare. If it does not match, do not trust what it says about the future.

---

## 2. Three studies

| Study | Who | Core question | How we check it |
|---|---|---|---|
| [1. University](docs/university.md) | Students, professors, campus recruiters | If AI cannot be banned, what does a university become? | Replay spring 2023, when ChatGPT arrived on campus |
| [3. Interviews](docs/interview.md) · [web app](https://claude.ai/artifact/9iyEj9ZfipFRNYMbEffmcc) | Job-seeking students, HR, technical interviewers | Who gets hired: the student with deep subject knowledge, or the one who is great with AI? | Real recruiters blind-review simulated transcripts |
| [2. Early career](docs/early-career.md) (paused) | People 0–3 years into work, senior staff, managers | Once AI can do junior work, how do newcomers grow into experts? | Replay 2023–2025, when junior hiring fell in AI-exposed jobs |

The three studies are three stops on one road: university, the interview, the first year at work. **Study 3 is built as a web app**, Interview Room 2030, with its source in `web/`. Study 2 is paused because it mostly takes the employer's point of view.

---

## 3. Run the Interview Room

There are three ways to run it. The dialogue can come from Claude, from DeepSeek, or from built-in templates.

| Where | Who writes the dialogue | Cost |
|---|---|---|
| The [claude.ai link](https://claude.ai/artifact/9iyEj9ZfipFRNYMbEffmcc) | Claude, on each viewer's own Claude plan | No per-call bill; uses the viewer's plan limits |
| `web/server.py` on your computer | DeepSeek, with your API key | Billed to your DeepSeek account; the page shows the running cost |
| Any of the above, in Demo mode | Templates and a fixed scoring formula | Free |

### Run it locally with DeepSeek

You need Python 3.9 or newer. Nothing else needs installing.

1. Make a file named `.env` in the repository folder with one line, using your own key:

   ```
   DEEPSEEK_API_KEY=sk-your-key-here
   ```

   `.env` is listed in `.gitignore`, so the key is never committed. Do not put the key anywhere else in the code.

2. Start the server:

   ```bash
   python3 web/server.py
   ```

3. Open <http://127.0.0.1:8000>. The mode switch in the top right shows **DeepSeek**.

The server only listens on your own computer by default. The key never reaches the browser: the page sends prompts to the server, and the server calls DeepSeek.

**Watching the cost.** The Hiring stats tab shows what this session and all runs since the last reset have cost, using the token counts DeepSeek reports. Set a spending cap there and runs stop before passing it. For a hard stop on the server side as well, add `DEEPSEEK_MAX_SPEND=0.50` to `.env`. Prices default to $0.28 per million input tokens and $0.42 per million output tokens. DeepSeek changes its prices, so check its pricing page and edit the numbers in the page or set `DEEPSEEK_PRICE_IN` and `DEEPSEEK_PRICE_OUT` in `.env`.

For reference, one round with two candidates took 5 calls and about 5,000 tokens, roughly $0.002 at those prices. A round with four candidates takes 9 calls.

### Preview without any model

```bash
python3 web/preview.py
```

This writes `web/preview.html`, which opens in any browser and runs in Demo mode.

---

## 4. How it is built

- **Text first, map second.** The core is the logic; the pixel room is how it is shown.
- **The model decides what to say; code decides how well it went.** Each candidate has hidden ability scores, and code turns them into the outcome of each step. The model only acts that outcome out. Differences between conditions then come from the design, not from model randomness.
- **Event-driven.** Only key moments are simulated, such as an interview step, a task or a debrief, not every hour.
- **Many runs, not one.** Each condition runs many times with different random seeds and fresh candidate variants, and we compare distributions with confidence intervals.
- **Interview the agents at the end** for qualitative material.

---

## 5. Known risks

- **Agents are too similar and too nice.** Language models converge. Personas need deliberate differences, stubbornness and noise.
- **Agents are too capable.** A language model knows everything, so it plays students and juniors as too strong. Whether someone "can do it" must be decided by an ability score in code, not by the model.
- **Agents recite op-eds.** Ask an agent about AI and it repeats commentary. Prompts must force concrete first-person decisions, such as "do I ask a colleague or the AI first?"
- **AI favors AI.** Language models acting as judges prefer AI-written text. Wherever an agent judges, real people should blind-review a sample for calibration.
- **Results mostly reflect the assumptions.** Keep every assumption in configuration and run sensitivity checks to see which conclusions are fragile.
