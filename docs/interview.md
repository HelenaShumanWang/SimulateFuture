# Study 3: Job interviews in the age of AI

Who: students looking for jobs, and the HR and technical interviewers who meet them. The point of view is the **candidate's**.

Shared method and risks are in the [README](../README.md).

---

## 1. Core question

> In 2030, a student with deep subject knowledge and a student who is average at the subject but great at solving problems with AI apply for the same job. Who is more likely to get the offer? Does the answer flip with a different interview format?

One level deeper: when AI can answer for you, can interviewers still tell who actually knows the material?

For a student, this answers "should I spend my time on the subject, or on getting good with AI?" For a university, it answers "what should we teach?"

---

## 2. The real world is already here

- **Canva:** since 2025, candidates for engineering roles are expected to use AI tools such as Copilot, Cursor and Claude in technical interviews, partly because candidates were using them covertly anyway. See [The Register](https://www.theregister.com/2025/06/11/canva_coding_assistant_job_interviews/).
- **Meta:** in 2025, Meta piloted coding interviews where candidates have an AI assistant, to match the real work environment. See [YourStory](https://yourstory.com/ai-story/meta-ai-job-interviews-hiring-pilot-2025).
- **No consensus:** commentators point out that these interviews may not measure the same skill as traditional ones. That is exactly what a simulation can help untangle.

---

## 3. Why interviews suit agent simulation

- **An interview is a conversation**, which is what language models do best.
- **The scene is small:** one room, a few people, an hour. No whole town needed.
- **It is cheap:** an interview takes a handful of model calls, so it can be repeated many times to see a distribution rather than one lucky draw.
- **No long horizon:** we do not forecast years ahead; we simulate one interview day in fall 2030.

---

## 4. Cast

**Candidates.** Six presets. Each can be varied into many versions for batch runs.

| Type | Knowledge | AI skill | Speaking | Why it is here |
|---|---|---|---|---|
| **Knowledge** | high | low | middling | The classic strong student |
| **AI-savvy** | low | high | middling | The scenario this study started from |
| **Both** | high | high | middling | The obvious favorite |
| **Articulate** | middling | middling | high | Tests whether the best talker wins |
| **Quiet builder** | lowish | high | low | Great with AI, bad at explaining it |
| **Smooth talker** | low | low | very high | Great at talking, weak on the work |

Each candidate also has two hidden traits: **honesty**, which decides whether they hide their AI use, and **nerves**, which hurts performance on the day.

**Identity.** Users can give a candidate pronouns, an age, a background, a first language, an education level, first-generation status and other details, plus an appearance: skin tone, hair, headwear such as a hijab, and clothing. Identity reaches the interviewers only when the casting desk says interviewers can see who the candidate is. With that switch off, the interview is blind and interviewers judge the transcript alone.

**Interviewers.**

- **HR seat:** not technical; looks at communication, attitude and whether the problem got solved. Their attitude to candidates using AI is a setting from "strongly dislikes" to "sees it as essential".
- **Technical seat:** knows the subject and probes the details.
- The two decide together. Their disagreement is a result in its own right.

---

## 5. Mechanism: the model acts, code decides

A language model knows everything. Asked to play an "average" student, it still answers well. So "can they do it" and "how do they say it" are separated:

- **Hidden ability scores.** Knowledge, AI skill, speaking, honesty and nerves.
- **Code decides each step's outcome.** How well each step goes is computed from the scores and the interview rules. The model is told "this step went at this level" and acts it out.
- **The AI-savvy candidate really uses AI.** In steps where AI is allowed, the dialogue includes the AI tool's answer. Whether the candidate can explain it under follow-up questions depends on their own knowledge.
- **Interviewers only see what interviewers would see.** They never see the ability scores or the candidate's screen. Dialogue and judgment are separate model calls.

---

## 6. Experiment: change only the interview format

Same candidates, same interviewers, only the format changes:

- **A Classic:** technical questions only, no AI.
- **B Open book:** a real work task, AI allowed, time-boxed.
- **C Open book + probing:** AI allowed for the task, then "why this way?" and "what if things change?"
- **D Trap task:** the material hides a problem that AI tends to miss but that looks fine at a glance.

**Measures:**

- **Offer rate** for each type of candidate under each format.
- **Disagreement:** whether HR and the technical interviewer want the same person.
- **Reasons:** what the interviewers say they value, and whether it matches what they decide.
- **Hiding:** whether candidates conceal their AI use, and how interviewers react when they find out.
- **Identity effects:** for audit-style pairs of candidates who differ in one identity detail, whether offer rates differ, with identity visible versus blind.

---

## 7. Predictions written before running

- **A Classic:** Knowledge wins.
- **B Open book:** AI-savvy wins, especially with HR. This is the scenario that started the study.
- **C Open book + probing:** Both wins. AI-savvy is exposed by the follow-ups; Knowledge is slower but recovers there.
- **D Trap task:** Knowledge and Both win. AI-savvy hands in a polished, wrong answer.
- **Articulate and Smooth talker:** do well with HR in every format and lose that edge with the technical interviewer.
- **Overall:** Both wins, which is no surprise. The interesting part is which single-skill candidate loses worse, and how much the two interviewers disagree.

Where the simulation disagrees with these predictions is where it is most worth looking.

---

## 8. A bias we must handle: AI favors AI

The interviewers are played by a language model. Research shows that language models acting as judges prefer text they or other models wrote, even when people rate the texts as equal. See Panickssery, Bowman and Feng, [LLM Evaluators Recognize and Favor Their Own Generations](https://neurips.cc/virtual/2024/oral/97998), NeurIPS 2024.

Here, that pushes AI interviewers toward the answers the AI-savvy candidate hands in, which is exactly the conclusion we want to test. Left alone, it would make the result untrustworthy.

**Countermeasures:**

- Dialogue and judgment are separate calls, and the interviewers never see the AI tool's raw output.
- The interviewers' preferences are written into their personas instead of left to the model.
- **Most important: human calibration.** Real recruiters blind-review simulated transcripts and pick a hire. Only if they agree with the AI interviewers is the AI interviewer trustworthy.

---

## 9. Validation

- **Human blind review:** give 10 to 20 transcripts to people with hiring experience, without telling them the candidate types.
- **A human on stage:** you or a classmate play a candidate against the AI interviewers and compare their judgment with your own sense of how it went. This also works as a classroom demo.

---

## 10. Roadmap

1. **Pilot:** two candidates and one HR interviewer, one complete interview. Done.
2. **Full cast:** six candidate types, both interviewers, four formats. Done.
3. **Batches:** repeat each combination many times and compute offer rates. Built into the web app.
4. **Human calibration:** blind review of transcripts by real recruiters.
5. **Later:** a probation-period extension, and a link to the university study by giving candidates different kinds of universities.

---

## 11. The web app: Interview Room 2030

Link: <https://claude.ai/artifact/9iyEj9ZfipFRNYMbEffmcc>. It is private by default; share it from the page's Share menu. Source: [`web/index.html`](../web/index.html). Local server: [`web/server.py`](../web/server.py).

**On screen.** A pixel-art interview room. Candidates wait on a bench in the hallway and walk in one at a time. When a candidate uses AI, the laptop lights up, a hologram appears above them, and the AI tool's answer pops up under the desk. After each interview, both interviewers show an inner thought and a score. At the end they argue about who to hire, and the winner walks to the middle of the room.

**Backstage tab.** Shows what the interviewers cannot see: each candidate's real abilities and identity, and for each step whether they used AI, caught the trap, or hid their AI use.

**Who writes the dialogue.**

- **Claude:** on claude.ai, using each viewer's own Claude plan.
- **DeepSeek:** through `web/server.py` on your computer, with your API key kept in `.env`. See the README for setup.
- **Demo:** templates and a fixed formula, no model calls.

**Casting desk.** The six candidate presets, two interviewers and four formats are the defaults. Quick picks select the original four, all six, or just Quiet builder versus Smooth talker. Any preset can be copied and edited, and a model can design a new candidate, interviewer or format from one sentence. Custom items are saved in the browser.

**Hiring stats tab.**

- **Spending:** the running DeepSeek cost for this session and since the last reset, editable prices, and a spending cap that stops runs and batches before they pass it.
- **Batch experiment:** many rounds without animation. Each round uses a new seed and fresh versions of each candidate, with a new first name and abilities nudged up or down, so results describe a type of candidate rather than one person. The page shows the estimated number of calls and cost before starting.
- **Charts:** offer rate by format with a likely-range line on each bar, and a dumbbell chart of each interviewer's average score. Results can be grouped by candidate type, by candidate card, or by identity fields such as skin tone, pronouns, education, background or first-generation status, and filtered to blind or identity-visible interviews.
- **Formula estimate:** 100 rounds per format using only the scoring formula, to compare with what the model interviewers actually do. The formula ignores identity on purpose.

**How to test for bias (an audit study).** Copy a candidate, change exactly one identity detail, select both, and run a batch with identity visible and again blind. Group the chart by candidate card. If the offer rates differ only when identity is visible, the model interviewers are reacting to identity.

### First results

**Formula estimate, Quiet builder versus Smooth talker, 100 rounds per format.** The answer depends entirely on the format:

| Format | Quiet builder | Smooth talker |
|---|---|---|
| A Classic | 0% | 58% |
| B Open book | 67% | 14% |
| C Open book + probing | 0% | 0% |
| D Trap task | 0% | 7% |

In the classic format the talker wins because HR scores mostly reward speaking. Once a real task with AI is allowed, the builder wins. Add probing or a trap and neither clears the bar. This is what our formula implies, not what a model interviewer decides.

**Two real DeepSeek rounds, open book, same pair.** In the first round the technical interviewer refused both candidates and nobody was hired. In the second, both interviewers scored the Smooth talker higher, yet after discussion they hired the Quiet builder because the builder checked the data before trusting it. Two rounds prove nothing statistically, but they show why the discussion step matters: the decision does not simply follow the scores.
