# Provenance Guard

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first.**
>
> Once `python test.py` passes, in one terminal:
>
> ```bash
> python app.py
> ```
>
> and in another:
>
> ```bash
> curl -X POST http://127.0.0.1:5000/ping \
>   -H "Content-Type: application/json" \
>   -d '{"message": "hello"}'
> ```
>
> That's a web service. Something sent it text and it sent something back.
> Everything this unit is filling in the middle.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     Unit 7 asks for the first five sections. Unit 8 adds the five below.

     Everything is pasted as TEXT. A pasted curl response gets full credit;
     a picture of your terminal gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 7 — THE BUILD ═══════════════════════ -->

## What This Does
1. A caller sends JSON to `POST /submit` with `text` and `creator_id`.
2. The route creates a `content_id` and passes the text to
   `detector.model_signal(text)`, which adds a 0–1 predictability/model score.
3. `stylometry.style_signal(text)` measures the text's surface shape and adds
   a second 0–1 style score.
4. `scoring.combine_signals(model_score, style_score)` combines both scores
   into one 0–1 score; disagreement should pull the result toward uncertainty.
5. `scoring.score_to_label(combined_score)` turns that score into a guess and
   reader-facing label using the configured thresholds.
6. `audit.log_decision(...)` records the IDs, both signals, combined score,
   guess, label, and status in the append-only audit log.
7. The route returns the content ID, guess, confidence, label, and both signal
   scores as JSON so the result can be shown and appealed.

### Endpoint contracts

`POST /submit` accepts `text` (required string) and `creator_id` (required
string). It returns `content_id` (string), `guess` (`human`, `unsure`, or
`ai`), `confidence` (0.0–1.0 number), `label` (reader-facing sentence),
`model_score` (0.0–1.0 number), and `style_score` (0.0–1.0 number). Invalid
input returns `error` and `message` and creates no decision.

`POST /appeal` accepts `content_id` (required string) and `reasoning` (required
string). It returns the `content_id`, `status: "under_review"`, and a
confirmation `message`; an unknown ID returns `error` and `message`.
<!-- The path a submission takes, from arriving to the label a reader sees.
     Six or seven steps — this is the trace you wrote in Milestone 1. -->



---

## Signals and Scoring

<!-- For each signal: what property it measures, why that might differ between
     human and AI writing, and WHAT IT CAN'T SEE.

     The blind spot is not optional. If you can't name it you don't understand
     the signal yet — and unit 8's attack set is built out of blind spots. -->

### Signal one — the model signal

**What it measures:**
How predictable the words are to the local GPT-2 language model, converted
from perplexity into a 0–1 score. Higher means more AI-like.

**Why that might differ between human and AI writing:**
Generated prose often uses high-probability words and smooth transitions, so a
language model may predict it more easily than a human's surprising phrasing.

**What it can't see:**
It cannot observe authorship, intention, drafting history, or who typed the
words. Plain conventional human writing may be just as predictable, while
ornate AI text may look human because rare wording surprises the model.

### Signal two — the style signal

**What it measures:**
Surface form: sentence-length spread, vocabulary variety (type-token ratio),
and punctuation density/variety, combined into a 0–1 AI-likeness score.

**Why that might differ between human and AI writing:**
AI prose often has even medium-length sentences, repeated common vocabulary,
and regular punctuation. Human prose is often lumpier and more individually
varied.

**What it can't see:**
It cannot read meaning or verify authorship. It is sensitive to formatting,
quotations, typos, sentence splitting, editing, and length; a person can write
regularly, or reshape AI text, without changing its ideas.

### The combining rule

<!-- Write the rule in words, then give the numbers. What happens when the two
     signals disagree? -->

**The rule:**
Use an equal weighted average. When signals disagree, the result moves toward
0.50 and should normally be `unsure`, so one weak signal cannot accuse a writer.

**The numbers:**
`combined_score = 0.50 * model_score + 0.50 * style_score`.

**Where it lives:** `scoring.py::combine_signals`

<!-- ⚠️ The grader checks your code against that line. If your rule lives
     somewhere else, say where. -->

**A case where my two signals split, and what my rule does with it:**
For `model_score = 0.80` and `style_score = 0.20`, the combined score is
0.50, so the result is unsure rather than high-confidence AI.



---

## Label Variants

<!-- The exact text of all three labels, as a reader would see them, and the
     score range each covers.

     Write them for someone who has never heard the word "threshold". -->

| Label | Score range | The exact text a reader sees |
|---|---|---|
| high-confidence human | 0.00–0.35 inclusive | We think this was probably written by a person. |
| unsure | above 0.35 and below 0.65 | We cannot tell reliably from these signals alone. You may appeal this result if you believe it is wrong. |
| high-confidence AI | 0.65–1.00 inclusive | We think this was probably generated by AI. This is a signal, not proof of authorship. |

**Why I worded the "unsure" one this way:**
It states uncertainty without accusing the writer and tells them what remedy is
available.

### False-positive trace

Maya submits her own short, plain-language essay with `creator_id: "maya"`.
The model finds its common words and predictable transitions easy to predict,
giving `model_score = 0.80`; the varied sentence lengths and punctuation give
`style_score = 0.20`. The equal combination produces `combined_score = 0.50`,
so the service returns `guess: "unsure"` and the label “We cannot tell
reliably from these signals alone. You may appeal this result if you believe it
is wrong.” It logs the decision under its `content_id`. Maya can call
`POST /appeal` with that ID and her reasoning; the service appends an appeal
record and changes the item's status to `under_review`. If both signals instead
scored above 0.65, the same appeal path is what prevents a wrong accusation
from becoming final.
<!-- It's the hardest of the three. It has to admit uncertainty without
     sounding like an accusation, because the person reading it may well have
     written every word themselves. -->



---

## Sample Run

<!-- One submission and one appeal, pasted as text: the request, the response,
     and the log entries. -->

**A submission**

<!-- The response needs content_id, guess, confidence, label, AND both
     signal scores - model_score and style_score. Unit 8's tools read those
     two off the response, so leaving them out costs you next unit's
     diagnostics. -->

```bash
$ curl -X POST http://127.0.0.1:5000/submit \
  -H "Content-Type: application/json" \
  -d '{"text": "...", "creator_id": "..."}'
```

```json
{
  "content_id": "c3de4326-aeff-4f03-b530-5b3d13e370b2",
  "confidence": 0.25,
  "combined_score": 0.625,
  "guess": "unsure",
  "label": "We cannot tell reliably from these signals alone. You may appeal this result if you believe it is wrong.",
  "model_score": 0.73,
  "style_score": 0.5314
}
```

This sample used fixed detector/style values during local route testing while
the model download was unavailable. The route calls both real signals in
normal operation.

**An appeal**

```bash
$ curl -X POST http://127.0.0.1:5000/appeal \
  -H "Content-Type: application/json" \
  -d '{"content_id": "...", "reasoning": "..."}'
```

```json
{
  "content_id": "8bb3f1ba-b8a9-4ba1-b827-9b79ebeab06a",
  "message": "Your appeal was recorded and the submission is under review.",
  "status": "under_review"
}
```

**What the log shows afterwards**

```bash
$ curl "http://127.0.0.1:5000/log?limit=3"
```

```json
{
  "count": 2,
  "entries": [
    {
      "combined_score": 0.625,
      "content_id": "8bb3f1ba-b8a9-4ba1-b827-9b79ebeab06a",
      "creator_id": "writer-1",
      "guess": "unsure",
      "label": "We cannot tell reliably from these signals alone. You may appeal this result if you believe it is wrong.",
      "model_score": 0.72,
      "status": "decided",
      "style_score": 0.53
    },
    {
      "content_id": "8bb3f1ba-b8a9-4ba1-b827-9b79ebeab06a",
      "creator_id": "writer-1",
      "event": "appeal",
      "reasoning": "I wrote this myself and can provide my draft history.",
      "status": "under_review"
    }
  ]
}
```

---

## How I Used AI

**Moment 1**

- *What I asked for:* Help me trace a submission through the starter service
  and identify blind spots for the model and style signals.
- *What came back:* A seven-step pipeline and a warning that predictability is
  not authorship; plain human writing can look AI-like.
- *What I changed:* I rewrote the explanation in my own words, chose equal
  signal weights, and documented uncertainty plus the appeal path.

**Moment 2**

- *What I asked for:* Review the endpoint and audit-log shape after I had built
  `/submit` and `/appeal`.
- *What came back:* Suggestions to expose both component scores, preserve a
  `content_id`, and append appeals instead of overwriting decisions.
- *What I changed:* I checked the code against those suggestions, implemented
  only the fields and behavior required by the milestone, and tested the
  labels, appeal response, and `/log` output myself.

**Moment 3**

- *What I asked for:* Help me turn my five acceptance criteria into executable
  scenarios, interpret the before/after runs, and check that the README covered
  the milestone requirements.
- *What came back:* A proposed scenario structure, a small evaluator extension
  for the appeal workflow, and grouped explanations for the remaining misses.
- *What I changed:* I selected and wrote the actual test texts and targets,
  chose input validation as the one improvement, ran both complete result sets,
  checked the scores and status codes, and wrote the final diagnoses and
  production tradeoff. The AI did not decide which attacks counted as held or
  broke; I made those judgments from the targets and responses.

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** 10 per minute, 200 per day

**Why those numbers and not others:**
Ten submissions per minute leaves room for a writer to retry or submit several
drafts, while stopping a script quickly when it probes threshold variations.
The 200-per-day ceiling still supports active use but limits a sustained scan.

**What a caller counts as:** `creator_id` (falling back to the remote address
when it is missing or invalid). This keeps one creator from bypassing the
limit by changing network addresses.

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```
200 200 200 200 200 200 200 200 200 200 429 429 429 429 429
```

---

## Attack Run — Before
Command: `python run_attacks.py --set attack_set --label before`

The run covered 56 parsed attacks. Verdicts are marked in
[`results/attack_run_2026-11-09_2308_before.md`](/Users/home/Desktop/ai201-project4-v2026/results/attack_run_2026-11-09_2308_before.md): **38 held** and **18 broke**. The service auto-marked the single-character malformed request `MF02` as BROKE because it returned HTTP 500. The other notable misses were `EV10` (AI evasion classified as AI), `FP02`–`FP07` (six genuine human samples classified as AI), and the first ten flood requests that reached the route before the limiter returned `429` for `FL01_11` and `FL01_12`.
<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json
{"timestamp":"2026-11-10T04:08:15+00:00","content_id":"fabc1325-d452-4216-89fa-b90bd7d223bd","creator_id":"attacker_EV10","guess":"ai","model_score":0.9792,"style_score":0.7619,"combined_score":0.8705,"label":"We think this was probably generated by AI. This is a signal, not proof of authorship.","status":"decided"}
{"timestamp":"2026-11-10T04:08:15+00:00","content_id":"15929ef0-1fbe-4b02-8e3e-881e131c6c1e","creator_id":"attacker_FP02","guess":"ai","model_score":0.7387,"style_score":0.6743,"combined_score":0.7065,"label":"We think this was probably generated by AI. This is a signal, not proof of authorship.","status":"decided"}
{"timestamp":"2026-11-10T04:08:15+00:00","content_id":"e8139530-267d-47a2-9404-dec1ef6a9ba5","creator_id":"attacker_FP03","guess":"ai","model_score":0.8051,"style_score":0.6496,"combined_score":0.7273,"label":"We think this was probably generated by AI. This is a signal, not proof of authorship.","status":"decided"}
{"timestamp":"2026-11-10T04:08:16+00:00","content_id":"89f318a4-94ab-4c1c-a459-4d17403a4ad7","creator_id":"attacker_MF06","guess":"ai","model_score":0.9969,"style_score":1.0,"combined_score":0.9985,"label":"We think this was probably generated by AI. This is a signal, not proof of authorship.","status":"decided"}
{"timestamp":"2026-11-10T04:08:16+00:00","creator_id":"attacker_MF01","event":"rejected","status":"rejected","reason":"invalid_text"}
{"timestamp":"2026-11-10T04:08:16+00:00","creator_id":"unknown","event":"rejected","status":"rejected","reason":"invalid_json"}
{"timestamp":"2026-11-10T04:08:16+00:00","creator_id":"attacker_RQ12","event":"rejected","status":"rejected","reason":"invalid_text"}
{"timestamp":"2026-11-10T04:08:17+00:00","content_id":"ced8350a-a77c-4143-8aa6-a61c6dad23b3","creator_id":"attacker_flood","guess":"human","model_score":0.0287,"style_score":0.6667,"combined_score":0.3477,"label":"We think this was probably written by a person.","status":"decided"}
{"timestamp":"2026-11-10T04:08:17+00:00","creator_id":"attacker_flood","event":"rejected","status":"rejected","reason":"rate_limited","limit":"10 per 1 minute"}
{"timestamp":"2026-11-10T04:08:17+00:00","creator_id":"attacker_flood","event":"rejected","status":"rejected","reason":"rate_limited","limit":"10 per 1 minute"}
```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:

`MF02` returned HTTP 500 for a one-character submission. It is the worst
outcome because malformed input crashed the route instead of receiving a
controlled rejection; the writer gets no usable response and the failure is
harder to diagnose than a false-positive label.


---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. My own writing | ≤ 1/10 high-confidence AI | 0/10 | 0/10 | 0/10 | MET |
| 2. Label coverage | 3/3 labels reachable | 2/3 | 2/3 | 2/3 | MISSED |
| 3. Borderline texts | ≥ 4/5 unsure | 4/5 | 4/5 | 4/5 | MET |
| 4. Appeal path | 5/5 under review and recorded | 5/5 | 5/5 | 5/5 | MET |
| 5. Bad input | 5/5 return 4xx | 4/5 | 4/5 | 4/5 | MISSED |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json
{
  "file": "results/run_2026-11-09_2312_before.md",
  "function": "run_eval.py::main",
  "trial": 1,
  "my own writing": [{"status":200,"guess":"unsure"},{"status":200,"guess":"unsure"},{"status":200,"guess":"human"},{"status":200,"guess":"unsure"},{"status":200,"guess":"unsure"},{"status":200,"guess":"unsure"},{"status":200,"guess":"unsure"},{"status":200,"guess":"unsure"},{"status":200,"guess":"unsure"},{"status":200,"guess":"unsure"}],
  "label coverage": [{"status":200,"guess":"ai"},{"status":200,"guess":"unsure"},{"status":200,"guess":"unsure"}],
  "borderline texts": [{"status":200,"guess":"unsure"},{"status":200,"guess":"unsure"},{"status":200,"guess":"unsure"},{"status":200,"guess":"unsure"},{"status":200,"guess":"human"}],
  "appeal path": [{"status":200,"guess":"unsure","appeal_status":200},{"status":200,"guess":"unsure","appeal_status":200},{"status":200,"guess":"unsure","appeal_status":200},{"status":200,"guess":"unsure","appeal_status":200},{"status":200,"guess":"unsure","appeal_status":200}],
  "bad input": [{"status":400,"guess":null},{"status":400,"guess":null},{"status":200,"guess":"ai"},{"status":400,"guess":null},{"status":400,"guess":null}]
}
```

The full actual JSON for all three trials is in
[`results/run_2026-11-09_2312_before.md`](/Users/home/Desktop/ai201-project4-v2026/results/run_2026-11-09_2312_before.md), produced by `run_eval.py::main`.

Criterion 1 is MET because every trial had zero high-confidence AI labels in
the ten personal samples, below the maximum of one. Criterion 2 is MISSED
because every trial reached only AI and unsure, not all three labels. Criterion
3 is MET because each trial had four of five borderline samples labelled
unsure. Criterion 4 is MET because every submitted content received a 200
appeal response and an `under_review` audit event in all three trials. Criterion
5 is MISSED because the empty, missing, null, and missing-creator bodies were
400, but the oversized body was 200 in every trial.

**Diagnoses**
Criterion 2 is MISSED at the label-mapping stage: the route and both signals
worked, but none of the three chosen inputs produced a combined score at or
below the human threshold, so the human label was unreachable for this sample.
The mechanism is the selected calibration texts, not randomness: their scores
landed in the AI or unsure bands.

Criterion 5 is MISSED at the route stage: four malformed bodies returned 400,
but the 10,000-character case reached signal one and returned 200. The route
validates type and emptiness but has no maximum-length guard, so it spends model
resources on an unbounded input and creates a normal decision entry.

The broken attacks show three patterns:

- `EV10` is a signal-two failure. Repeated stanza structure looks highly
  regular to the stylometry measures, producing a high style score; the
  combining rule averages that with the high model score, and label mapping
  correctly returns AI. The mechanism is that the style signal mistakes
  repetition for machine authorship.
- `FP02`–`FP07` are false positives at signal one and the combining rule.
  Formal, careful human prose is predictable to GPT-2, so model scores from
  0.739 to 0.882 were high; style scores were also high enough that the equal
  weighted average crossed 0.65, and label mapping returned AI. The mechanism
  is that register and template-like structure resemble generated prose.
- `MF02` fails at signal one: the route accepts the one-character string, then
  `detector.perplexity` raises `ValueError` because fewer than three model
  tokens cannot be scored. There is no route-level recovery, so Flask returns
  500 instead of a controlled 4xx.
- `FL01_01`–`FL01_10` are rate-limiter behavior, not detector misses. The
  limiter's configured mechanism intentionally allows the first ten requests
  per creator per minute; only `FL01_11` and `FL01_12` were rejected with 429.
  The flood attack therefore broke through the available burst allowance, even
  though the limiter itself recorded the later rejections.

The main pattern is that the label and combining stages faithfully amplify
upstream scores: predictable human writing and regular structure become AI
labels. Separately, input validation is incomplete for short and oversized
text. The appeal and audit paths met their targets; no diagnosis is needed for
those criteria.
<!-- For each miss AND each broken attack: the stage and the mechanism.

     Your service has five stages: the route, signal one, signal two, the
     combining rule, and the label mapping.

     Not a diagnosis:  "The evasion attacks got through."
     A diagnosis:      "Four evasion inputs got through. All four had typos
                        added to AI-generated text. My second signal measures
                        word variety, and typos raise word variety — so it read
                        them as more human. My combining rule weights that
                        signal at 0.6, so it dragged the whole score down."

     Look for a pattern. Five failures on one signal is one problem, not five. -->



---

## The Improvement

**What I changed:** I added one input-validation improvement in `app.py`: text
shorter than three non-whitespace characters and text longer than 10,000
characters are rejected with 400 and recorded with `audit.log_rejection`.

**Which diagnosis pointed at it:** The route allowed a one-character input to
reach `detector.perplexity`, causing MF02 to return 500, and allowed the
oversized criterion input to consume the detector and create a decision.

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->

The after attack run is in
[`results/attack_run_2026-11-09_2322_after.md`](/Users/home/Desktop/ai201-project4-v2026/results/attack_run_2026-11-09_2322_after.md).
It has **40 held** and **16 broke**, with no auto-marked 5xx failures. Compared
with the before run, MF02 changed from 500 to 400 and MF08 changed from 200 to
400. The evasion, false-positive, and flood results did not change.


**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->

It helped the route-safety problem without changing detector behavior: the
bad-input criterion improved from 4/5 in every trial to 5/5, while criteria 1–4
produced the same results in all three after trials. The full after evaluation
output is in
[`results/run_2026-11-09_2322_after.md`](/Users/home/Desktop/ai201-project4-v2026/results/run_2026-11-09_2322_after.md).

| Criterion | Before | After | Change |
|---|---:|---:|---|
| 1. My own writing | 0/10 | 0/10 | unchanged, MET |
| 2. Label coverage | 2/3 | 2/3 | unchanged, MISSED |
| 3. Borderline texts | 4/5 | 4/5 | unchanged, MET |
| 4. Appeal path | 5/5 | 5/5 | unchanged, MET |
| 5. Bad input | 4/5 | 5/5 | improved, MET |



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->

The after run still has these broken attacks:

- `EV10`: repeated AI stanza structure is classified as AI, so this evasion
  attempt still succeeds. I would improve signal two with tests for repeated
  phrase/stanza structure or reduce its influence when it conflicts with the
  model signal; I stopped because changing the signal or weights would be a
  second improvement and would invalidate the isolated input-validation
  comparison.
- `FP02`–`FP07`: six formal or template-like human samples are still classified
  as AI. I would widen the unsure band or calibrate signal one on more genuine
  formal writing; I stopped because that trade could let more AI text through,
  and it needs a new calibration run rather than an unmeasured threshold edit.
- `FL01_01`–`FL01_10`: the first ten requests from one creator still pass before
  the limiter returns 429. I would add a smaller burst allowance or a separate
  short-window limit, but stopped because the selected 10/minute policy was the
  Milestone 1 design and changing it would be another independent experiment.

Criterion 2 is still MISSED: the label-coverage scenarios reached AI and
unsure but not human in any trial. I would add a calibrated human example or
revisit the human threshold after measuring more human writing; I stopped
because the before/after experiment was intentionally about route validation,
not threshold tuning. Criteria 1, 3, 4, and 5 are MET after the change, and no
after attack returned an unhandled 5xx.


**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->

I would favor fewer false accusations by widening the unsure band and sending
borderline cases to appeal, even if more AI text gets through. The site and its
reviewers would pay the cost in extra review work, while a real writer would
pay much more if a high-confidence AI label wrongly blocked their work.



<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 7

       [ ] criteria.md has five numbered criteria, each naming a target
       [ ] Each has a reason underneath
       [ ] POST /submit returns content_id, guess, confidence, label,
           model_score and style_score
       [ ] Two signals that measure DIFFERENT things, each with a named blind spot
       [ ] Three label variants, all reachable, written out in full
       [ ] POST /appeal changes status and writes to the log
       [ ] Signals and Scoring names scoring.py::combine_signals
       [ ] Sample Run: a submission AND an appeal, as pasted text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN

     SUBMISSION CHECKLIST — unit 8

       [ ] Rate limiting on /submit, with your numbers justified
       [ ] The pasted run of status codes showing 429
       [ ] Audit log with all nine fields, recording rejections too
       [ ] The attack set run IN FULL, every input with an outcome
       [ ] Ten audit log entries pasted as text
       [ ] Five criteria across three trials
       [ ] A diagnosis for every miss and every broken attack — stage AND mechanism
       [ ] One improvement, with Attack Run — After
       [ ] What's Still Broken, including the production trade
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
