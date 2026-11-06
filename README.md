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

<!-- ═══════════════════════ UNIT 8 — THE TEST ═══════════════════════ -->

---

## Rate Limiting

**My limits:** ___ per minute, ___ per day

**Why those numbers and not others:**
<!-- Think about two people: a real writer submitting their own work a few
     times an hour, and a script sending a thousand variations to map your
     thresholds. Your numbers have to be liveable for the first and hostile to
     the second. -->

**What a caller counts as:** <!-- per address, or per creator_id? They fail
differently — one script can look like a thousand callers, and one household
can look like one. -->

**The run of status codes when I pushed past it:**

<!-- python run_attacks.py --flood 15 -->

```

```

---

## Attack Run — Before

<!-- Every attack with its outcome and a held-or-broke mark.
     `run_attacks.py --label before` produces the table. -->



**Ten audit log entries from the run**

<!-- Choose entries that show the interesting failures, not the ten easiest. -->

```json

```

**The single worst outcome** — the one I'd least want to explain to a writer
whose work got caught by it:



---

## Run Log and Verdicts

<!-- Your five criteria across three trials. `run_eval.py --label before`. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1.  |  |  |  |  |  |
| 2.  |  |  |  |  |  |
| 3.  |  |  |  |  |  |
| 4.  |  |  |  |  |  |
| 5.  |  |  |  |  |  |

**Real output from one trial**, pasted as text, naming the file and function
that produced it:

```json

```

**Diagnoses**

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

**What I changed:**

**Which diagnosis pointed at it:**

### Attack Run — After

<!-- Same format. `run_attacks.py --label after` -->



**Did it help, and how do I know:**

<!-- Widening the unsure band usually fixes one problem and creates another.
     Reporting that trade honestly is worth full credit. -->



---

## What's Still Broken

<!-- For each attack still getting through and each criterion still missed:
     what you'd do, and why you stopped. -->



**The trade I'd make if this ran for real:**

<!-- Two sentences. Fewer wrong accusations means more AI text getting through.
     Say which way you'd go and WHO PAYS FOR IT. -->



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
