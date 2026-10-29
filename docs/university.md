# Study 1: What will universities become in the age of AI?

Who: university students, professors, and the employers who recruit on campus.

Shared method and risks are in the [README](../README.md).

---

## 1. Core question

> If students use AI freely and banning it does not work, what does a university eventually become?
> When assignments and grades no longer prove what someone can do, what do students, professors and employers rely on to trust each other?

Why this question:

- **It links university to hiring.** Assignments, then grades, then a résumé, then an offer. AI breaks the first link, and every later link moves with it.
- **The premise is already nearly true.** AI can complete most coursework, detection is unreliable, and universities cannot ban it outright. What is uncertain is how people and institutions respond, which is what agent simulation is good at.
- **Both possible results are interesting.** It may turn out that real, in-person skill becomes more valuable, or that connections become more valuable than ability.

---

## 2. Our hypothesis: three possible end states

Today a university bundles four things:

1. Teaching knowledge
2. Certifying and screening for employers
3. A network of professors, classmates and alumni
4. A safe place for young people to try things and fail

AI unbundles the first one first, then shakes the second. The third and fourth cannot be replaced by AI and become relatively more valuable. The remaining pieces recombine into roughly three end states:

| End state | What the university mainly does | How students learn | What employers look at |
|---|---|---|---|
| **Testing center** | Proctors exams and issues credentials | Self-study with AI; come to campus only for exams | In-person exam results, certificates |
| **Apprentice workshop** | Runs real projects, often with companies | Small project teams with professors as coaches | Portfolio, project performance, mentor references |
| **Business as usual** | Same lectures and assignments; AI used freely | AI does the assignments; class becomes a formality | Grades stop working; internships and connections take over |

Different tiers of universities may end up in different places. Elite schools may become "network clubs plus workshops" while ordinary schools become testing centers. If so, AI would widen rather than narrow the gap between universities. That is what the simulation should test.

**What the simulation can and cannot answer:** it cannot say which end state universities will choose; that is decades of institutional change. It can say how people get along inside each end state, who benefits, and whether employers accept the result.

---

## 3. Time settings

Two kinds of "time" must be kept apart:

| | Setting | Reason |
|---|---|---|
| How long the simulation runs | One semester, about 15 weeks | A semester has natural milestones: start, midterms, finals, recruiting season. Run longer and agent personas drift, while cost grows linearly. |
| Which year is simulated | Fall semester 2029 | Students who started in fall 2026 are seniors, right in recruiting season. Within about five years AI capability can still be assumed sensibly; further out, the result is mostly the assumption itself. |

Instead of running ten years continuously, we take **snapshots**: set up the world of a given year and run one semester. To look further, build a 2035 snapshot with different parameters and treat it as structured science fiction, not a forecast.

---

## 4. Experiment 1: replay spring 2023

**World:** an ordinary university in fall 2022. In December, a chat tool that can write any assignment appears, and we simulate the spring 2023 semester. This round also covers the "ban it" phase, since many universities did try bans in early 2023.

**Compare with publicly reported changes:**

- Students adopted the tool quickly and widely, well before universities had rules.
- Universities moved from blanket bans to course-by-course policies.
- Handwritten in-class exams and oral exams came back.
- AI detectors produced many false positives, and non-native English speakers were wrongly accused more often.
- Professors grew suspicious of polished writing, and trust between students and professors fell.

**Caution:** the model was trained on 2023 news, so it may "remember" the outcome rather than reason its way there. Passing the replay is a minimum bar, not proof. What matters more is whether the process and mechanisms it shows are plausible.

---

## 5. Experiment 2: three universities in fall 2029

**Shared world rules:**

- AI can complete nearly all coursework, detection is unreliable, and the university does not ban it. Every student has an AI assistant and decides whether and how to use it.
- There are fewer entry-level jobs than today. How many fewer is a parameter for sensitivity analysis.
- The last two weeks of the semester are recruiting season, and employer agents choose among the students.

**Three conditions, three end states:** testing center, apprentice workshop, business as usual. Everything else is identical: the same personas and the same random seeds.

**Cast (pilot of about 12):**

- **8 students**, deliberately varied: first-generation or well connected; native or non-native speaker; strong or weak; outgoing or shy; attitude toward AI.
- **2 professors**: one embraces technology, one is skeptical.
- **1 teaching assistant.**
- **1 or 2 employers**, who appear for recruiting at the end of the semester.

**Measures:**

- **Trust:** between students and professors and among students, from weekly self-reports plus behavior: asking for help, collaborating, reporting.
- **Interaction:** time spent with people versus only with AI; whether study groups grow or shrink.
- **Proof:** how students prove themselves (grades, portfolio, references, connections) and what employers finally decide on.
- **Outcomes:** who gets an offer and who falls behind, and how that relates to their starting point (connections, language, ability).

---

## 6. Predictions written before running

- **Testing center:** almost no interaction between students and professors, and little among students. Exam results regain some signal, but employers still doubt they show real ability.
- **Apprentice workshop:** the most interaction and the most trusted by employers. But good projects and mentor time are scarce, and outgoing, confident native speakers get more of them.
- **Business as usual:** grades inflate across the board; employers stop trusting them and turn to internships and references, and well-connected students win.
- **Overall:** in all three, "someone who can vouch for you" becomes more valuable. The difference is who finds it easy to get.

Where the simulation disagrees with these predictions is where it is most worth looking.

---

## 7. Roadmap

1. **Pilot:** about 12 agents, one week, business-as-usual only, to get the loop running.
2. **Replay:** Experiment 1.
3. **Main experiment:** Experiment 2, three end states, several seeds each.
4. **Later:** more agents, a 2035 snapshot, visualization.
