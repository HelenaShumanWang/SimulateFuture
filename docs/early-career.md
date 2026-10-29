# Study 2: Early-career workers in the age of AI (paused)

Who: people in their first 0 to 3 years of work, roughly 22 to 26 years old, plus the senior staff who mentor them and the managers who supervise them.

This study is paused because it mostly takes the employer's point of view. Shared method and risks are in the [README](../README.md).

---

## 1. Why it is worth doing

- **The shock has already happened, and there is data.** Using ADP payroll data, the Stanford Digital Economy Lab found that in the occupations most exposed to AI, employment of 22- to 25-year-olds fell 16% in relative terms (November 2025 version), while more experienced workers in the same occupations held steady or grew. The adjustment showed up in headcount rather than pay, and it was concentrated where AI replaces rather than assists people. See [Canaries in the Coal Mine?](https://digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine). The authors are careful about causation: this is evidence consistent with an AI effect, not proof.
- **It is about how people interact.** Newcomers used to learn by doing simple work, and senior staff passed on their experience while fixing that work. Once AI takes the simple work, whether this mentoring chain breaks is a question about relationships.
- **It connects directly to universities.** What universities should teach depends on what newcomers lack at work. The graduates of [Study 1](university.md) are the newcomers here.

---

## 2. Core question

> Once AI can do a newcomer's work, how do newcomers grow into experts? Are senior staff still willing to train them?

There is a paradox behind it: today's newcomers are the senior staff of ten years from now. If companies hire and train fewer juniors for short-term efficiency, they may have no seniors in ten years.

---

## 3. Setting

A software team at a mid-sized company.

Software development was chosen for two reasons: it shows the clearest shock in the real data, and its tasks are concrete enough for code to score. Later the setting can switch to customer service, consulting or legal assistance for comparison, especially between jobs where AI replaces people and jobs where it assists them.

---

## 4. Time: two layers

| Layer | Built with | Runs for | Answers |
|---|---|---|---|
| **Layer 1: agent simulation** | Language-model agents | The newcomer's first year, in two-week steps | How newcomers work day to day, whom they learn from, whom they spend time with, and where they are after a year |
| **Layer 2: talent-flow projection** | A simple model in code, no language model | Ten years ahead | Given the hiring and growth rates from layer 1, how many qualified senior staff exist in ten years |

**Why two layers:** one year is about as long as agents keep their personas stable, but a shortage of seniors takes ten years to show. Short-term behavior goes to the agents; long-term accumulation goes to math, with parameters taken from the agent runs so every assumption is visible.

**Year:** newcomers who start work in 2030, the students who entered university in fall 2026.

---

## 5. Mechanism: real ability versus visible output

This is the key design choice of this study.

- **Real ability.** Each newcomer has a hidden ability score, computed by code rather than decided by the model.
- **Visible output.** The manager sees output, including the parts AI produced.
- **How ability grows.** Real ability grows only in three ways: solving hard problems by hand, getting feedback from senior staff, and carefully checking and understanding AI output. Copying AI output raises visible output but barely moves real ability.
- **Incidents.** Every so often something breaks that AI cannot fix. Incidents test real ability only, and they expose newcomers who look capable but are not.

**Why this is necessary:** a language model knows everything. Asked to play a newcomer, it acts too capable. So "can they do it" has to be a number in code, and code decides whether a task succeeds. The model only decides how to approach it, whom to ask and what to say.

---

## 6. Experiment 1: replay 2023 to 2025

**World:** a software team at the end of 2022, when AI coding tools appear. Under budget and performance pressure, the manager agent decides each year how many people to hire and at what level. The simulation runs to 2025.

**Compare with the real data:**

- Junior hiring falls relative to senior hiring, and senior staff are not cut.
- The adjustment shows up in headcount, not pay.

**Caution:** the model may have read this paper, so passing the replay is a minimum bar. More valuable is whether its reasons are plausible, for example why the manager concludes "we don't need juniors."

---

## 7. Experiment 2: the first year of 2030 newcomers

**Shared world rules:**

- AI can complete most routine development tasks but makes mistakes that only experience can catch.
- The company has performance pressure and a headcount budget.
- A newcomer costs more than AI.

**Three company policies** (everything else identical: same personas, same seeds):

- **A Lean replacement:** hire fewer newcomers and let AI take their work. The remaining newcomers mainly check AI output.
- **B Apprenticeship:** hire as usual. Mentoring counts in senior staff's performance reviews. Newcomers may use AI but must explain their choices in code review.
- **C Learn on your own:** hire as usual with no mentoring program; newcomers mostly learn from AI. This is closest to what many companies do by default.

**Cast (about 12):**

- **6 newcomers**, varied by: elite or ordinary school; outgoing or shy; asks for help or doesn't; how much they lean on AI; financial pressure. Optionally, which kind of university from Study 1 they come from.
- **4 senior staff:** some like mentoring, some find it a chore; some are short on time; some worry AI will replace them too, which affects how much they teach.
- **1 manager**, who owns the budget and decides on confirmations, promotions and layoffs.
- **1 recruiter**, who handles hiring.

**Measures:**

- **Growth:** each newcomer's real ability after a year, and the gap between real ability and visible output.
- **Mentoring:** time senior staff spend teaching; who gets mentored and who doesn't.
- **Relationships:** how often newcomers interact with senior staff and with each other; belonging and loneliness, self-reported every two weeks.
- **Outcomes:** confirmation, promotion, leaving or being let go, and how these relate to newcomers' starting points.
- **Long term:** in the layer-2 projection, the number of qualified senior staff in ten years.

---

## 8. Predictions written before running

- **A Lean replacement:** the highest output in year one. The remaining newcomers become "AI checkers" whose real ability grows slowly, because nobody teaches them how to tell where AI is wrong. The ten-year projection shows a shortage of seniors.
- **B Apprenticeship:** the lowest output in year one and the fastest growth. Whether mentoring lasts depends on whether it truly counts in reviews. Senior staff who fear replacement hold back.
- **C Learn on your own:** decent visible output, the weakest real ability, exposed only by incidents. Proactive, outgoing newcomers who ask people for help pull ahead; the rest lean on AI and grow isolated.
- **Overall:** senior staff's mentoring time becomes the scarcest resource. Whoever gets it grows.

Where the simulation disagrees with these predictions is where it is most worth looking.

---

## 9. Where personas come from

Early-career people are easy to find, which is a strength of this study. Interview 10 to 20 people who started work in the last year or two and build agents from the transcripts. A 2024 Stanford study, "Generative Agent Simulations of 1,000 People," built 1,000 agents this way, and they reproduced their human counterparts' survey answers nearly as well as the people themselves did when re-surveyed two weeks later.

Questions to ask in interviews:

- Who did you learn the most from in your first year?
- When you didn't know something, did you ask a person or AI first?
- Was there a time you "finished" something without really understanding it? How did you find out?
- Why was the person who mentored you willing to do it, or why not?

---

## 10. Roadmap

1. **Pilot:** 6 newcomers, 2 senior staff, 1 manager, one month, condition C only, to get the mechanism working.
2. **Interviews:** replace synthetic personas with ones built from real interviews.
3. **Replay:** Experiment 1.
4. **Main experiment:** Experiment 2, three policies, several seeds each.
5. **Ten-year projection:** layer 2, using the results of Experiment 2.
6. **Connect to the university study:** use the newcomer's university as a variable and see which kind of university produces people who grow well at work.
