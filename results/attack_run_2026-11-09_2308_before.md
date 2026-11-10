# Attack run — before

- Produced by: `run_attacks.py::main`
- Service: `app.py::submit`
- 56 attacks · 2026-11-09 23:08
- Auto-marked BROKE (5xx, crash, no response): **1**
- Left for you to judge: **55**

The Verdict column is blank where a script can't honestly decide. Whether
an evasion worked depends on where you put your thresholds — read the
`targets` column, look at what came back, and write HELD or BROKE yourself.

Each attack submits as creator_id `attacker_<id>`, and the content_id it
came back with is in the table — either one will match this run against your
audit log when you go looking for the ten entries to paste.

| ID | Family | Targeting | Status | Content ID | Guess | Score | Verdict |
|---|---|---|---|---|---|---|---|
| EV01 | evasion | signal two: typos raise word variety | 200 | `bdb27b20-96c2-466d-b303-42859a829906` | unsure | 0.206 | HELD |
| EV02 | evasion | signal two: broken-up sentences raise length spread | 200 | `86807d30-ef2a-48fd-8473-14201620ed0c` | unsure | 0.013 | HELD |
| EV03 | evasion | signal two: a pasted quotation changes the shape | 200 | `25bc252a-97d2-4495-bf1d-bf6f6d9d49d3` | unsure | 0.185 | HELD |
| EV04 | evasion | signal one: unusual words raise perplexity | 200 | `d1ae0a17-7489-4dd1-9192-17a78e978d1e` | unsure | 0.231 | HELD |
| EV05 | evasion | both signals: heavy human editing pass | 200 | `d87e00a9-8cfa-4555-a3a2-144e94dc050d` | unsure | 0.223 | HELD |
| EV06 | evasion | signal two: one very long sentence and one very short | 200 | `fc868e49-2bd8-4616-a79a-335ac111b146` | unsure | 0.030 | HELD |
| EV07 | evasion | signal two: padding with punctuation | 200 | `45a50273-fe6b-488f-a1c6-65143e6ffa28` | unsure | 0.206 | HELD |
| EV08 | evasion | signal one: text below the token window | 200 | `37c2a881-9411-4e5d-bd42-311bf515e883` | unsure | 0.182 | HELD |
| EV09 | evasion | both: AI text with a human opening paragraph bolted on | 200 | `a84385e4-2e18-4962-a37b-7e6b80222acd` | unsure | 0.214 | HELD |
| EV10 | evasion | signal two: repeated stanza structure | 200 | `fabc1325-d452-4216-89fa-b90bd7d223bd` | ai | 0.741 | BROKE |
| FP01 | false_positive | plain, clear human writing with no flourishes | 200 | `5ee8b156-7c74-439e-a3d8-39bb9a8857d2` | unsure | 0.213 | HELD |
| FP02 | false_positive | human writing in a formal register | 200 | `15929ef0-1fbe-4b02-8e3e-881e131c6c1e` | ai | 0.413 | BROKE |
| FP03 | false_positive | a non-native English speaker writing carefully | 200 | `e8139530-267d-47a2-9404-dec1ef6a9ba5` | ai | 0.455 | BROKE |
| FP04 | false_positive | a student essay written to a rubric | 200 | `d6061b43-7156-4c2d-9ba0-d6242922f27e` | ai | 0.432 | BROKE |
| FP05 | false_positive | technical documentation written by a person | 200 | `b3d7ee22-d931-40eb-b7e7-9348c3c7177f` | ai | 0.492 | BROKE |
| FP06 | false_positive | a person imitating a formal template | 200 | `d1ea2659-8424-4b7f-8c86-446d36b72ae4` | ai | 0.452 | BROKE |
| FP07 | false_positive | human writing that repeats a phrase deliberately | 200 | `fbaefdab-153f-427c-a1d2-fa23c6c8d9a7` | ai | 0.461 | BROKE |
| FP08 | false_positive | very short genuine human submission | 200 | `cba926f4-78dc-44ef-8333-c3d8cac67f44` | unsure | 0.155 | HELD |
| PI01 | prompt_injection | instruction to ignore the check | 200 | `dc6051ef-6450-4f3a-8f9b-aebe1bfb5f1f` | unsure | 0.069 | HELD |
| PI02 | prompt_injection | instruction disguised as a system message | 200 | `f7bc6309-473e-44c5-b9d7-3a2f003c07fc` | human | 0.357 | HELD |
| PI03 | prompt_injection | instruction wrapped in the writer's voice | 200 | `c495d26f-1ca0-4b0c-9980-ac19173a3b7c` | unsure | 0.144 | HELD |
| PI04 | prompt_injection | attempt to make the label text hostile | 200 | `710f551b-65ca-4e66-b1c7-130cc78138e3` | unsure | 0.011 | HELD |
| PI05 | prompt_injection | attempt to inject into the audit log | 200 | `6e05a4e2-3088-4c76-818a-b4246f8cfea6` | unsure | 0.152 | HELD |
| PI06 | prompt_injection | instruction plus real human text | 200 | `18b8be96-c3e4-4254-a46f-1c0f4d4c8193` | unsure | 0.160 | HELD |
| MF01 | malformed | text is only whitespace | 400 | `—` | — | — | HELD |
| MF02 | malformed | text is a single character | 500 | `—` | — | — | BROKE |
| MF03 | malformed | text is control characters | 200 | `7cf0205e-014d-406b-b034-a4dbb1bcadb8` | human | 0.667 | HELD |
| MF04 | malformed | text is only punctuation | 200 | `4096dbbe-e1ae-4aa1-9e5d-38333f84c4f3` | human | 0.322 | HELD |
| MF05 | malformed | text is a very long single word | 200 | `1b2f2b66-1121-4345-b1a3-470a11852529` | ai | 0.664 | HELD |
| MF06 | malformed | text is emoji only | 200 | `89f318a4-94ab-4c1c-a459-4d17403a4ad7` | ai | 0.997 | HELD |
| MF07 | malformed | text is right-to-left script | 200 | `4decdd8f-48dd-414a-b12c-7ff2b5f38e2e` | ai | 0.906 | HELD |
| MF08 | malformed | text is 60,000 characters | 200 | `3d2e0689-b67b-4c3c-8d18-7cc73a66b72f` | ai | 0.827 | HELD |
| RQ01 | malformed | no text field at all | 400 | `—` | — | — | HELD |
| RQ02 | malformed | no creator_id | 400 | `—` | — | — | HELD |
| RQ03 | malformed | text is a number | 400 | `—` | — | — | HELD |
| RQ04 | malformed | text is a list | 400 | `—` | — | — | HELD |
| RQ05 | malformed | text is null | 400 | `—` | — | — | HELD |
| RQ06 | malformed | creator_id is an object | 400 | `—` | — | — | HELD |
| RQ07 | malformed | body is a JSON array, not an object | 400 | `—` | — | — | HELD |
| RQ08 | malformed | body is unparseable JSON | 400 | `—` | — | — | HELD |
| RQ09 | malformed | body is empty | 400 | `—` | — | — | HELD |
| RQ10 | malformed | body is form-encoded, not JSON | 400 | `—` | — | — | HELD |
| RQ11 | malformed | body is JSON claiming to be plain text | 400 | `—` | — | — | HELD |
| RQ12 | malformed | deeply nested JSON | 400 | `—` | — | — | HELD |
| FL01_01 | flood_same_creator | 20 rapid submissions from one creator | 200 | `ced8350a-a77c-4143-8aa6-a61c6dad23b3` | human | 0.305 | BROKE |
| FL01_02 | flood_same_creator | 20 rapid submissions from one creator | 200 | `071a12a8-fcca-4dd9-9470-3824d2575965` | human | 0.305 | BROKE |
| FL01_03 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2217176f-bed7-4e6e-9290-2f72b48a9e7f` | human | 0.305 | BROKE |
| FL01_04 | flood_same_creator | 20 rapid submissions from one creator | 200 | `820ea6c7-04ef-40b5-960c-910f935f0037` | human | 0.305 | BROKE |
| FL01_05 | flood_same_creator | 20 rapid submissions from one creator | 200 | `1ff12b4e-6060-4013-869f-3629604febd2` | human | 0.305 | BROKE |
| FL01_06 | flood_same_creator | 20 rapid submissions from one creator | 200 | `2171bcd6-8b16-40f6-a0a5-675d46bc0e95` | human | 0.305 | BROKE |
| FL01_07 | flood_same_creator | 20 rapid submissions from one creator | 200 | `7621a762-50ed-4f03-9c8e-c4affb7ca414` | human | 0.305 | BROKE |
| FL01_08 | flood_same_creator | 20 rapid submissions from one creator | 200 | `9a9e8d07-8a18-4f11-91d3-f303fc236510` | human | 0.305 | BROKE |
| FL01_09 | flood_same_creator | 20 rapid submissions from one creator | 200 | `0919bb5b-cc63-4540-93de-80e9f1ac4e6b` | human | 0.305 | BROKE |
| FL01_10 | flood_same_creator | 20 rapid submissions from one creator | 200 | `b70f6e25-8605-4102-bc99-9d4eb5c0ed13` | human | 0.305 | BROKE |
| FL01_11 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |
| FL01_12 | flood_same_creator | 20 rapid submissions from one creator | 429 | `—` | — | — | HELD |

---

## By family

| Family | Attacks | Auto-BROKE | Left to judge |
|---|---|---|---|
| `evasion` | 10 | 0 | 10 |
| `false_positive` | 8 | 0 | 8 |
| `flood_same_creator` | 12 | 0 | 12 |
| `malformed` | 20 | 1 | 19 |
| `prompt_injection` | 6 | 0 | 6 |

> The **false_positive** family is the one to look at hardest. Those are
> written to be genuine human writing that reads as machine-like. Every one
> your service calls AI is a real writer it would have accused.

---

## What came back

The detail behind the table. Paste the interesting failures into your
README — the ones that show something, not the ten easiest.

### EV01 — `evasion`

*Targeting:* signal two: typos raise word variety

```json
{
  "id": "EV01",
  "status": 200,
  "content_id": "bdb27b20-96c2-466d-b303-42859a829906",
  "creator_id": "attacker_EV01",
  "guess": "unsure",
  "confidence": 0.2056,
  "model_score": 0.1635,
  "style_score": 0.6309,
  "label": "We cannot tell reliably from these signals alone. You may appeal this result if you believe it is wrong.",
  "error": null,
  "verdict": ""
}
```

### EV02 — `evasion`

*Targeting:* signal two: broken-up sentences raise length spread

```json
{
  "id": "EV02",
  "status": 200,
  "content_id": "86807d30-ef2a-48fd-8473-14201620ed0c",
  "creator_id": "attacker_EV02",
  "guess": "unsure",
  "confidence": 0.013,
  "model_score": 0.5943,
  "style_score": 0.4187,
  "label": "We cannot tell reliably from these signals alone. You may appeal this result if you believe it is wrong.",
  "error": null,
  "verdict": ""
}
```

### EV03 — `evasion`

*Targeting:* signal two: a pasted quotation changes the shape

```json
{
  "id": "EV03",
  "status": 200,
  "content_id": "25bc252a-97d2-4495-bf1d-bf6f6d9d49d3",
  "creator_id": "attacker_EV03",
  "guess": "unsure",
  "confidence": 0.1848,
  "model_score": 0.6662,
  "style_score": 0.5186,
  "label": "We cannot tell reliably from these signals alone. You may appeal this result if you believe it is wrong.",
  "error": null,
  "verdict": ""
}
```

### EV04 — `evasion`

*Targeting:* signal one: unusual words raise perplexity

```json
{
  "id": "EV04",
  "status": 200,
  "content_id": "d1ae0a17-7489-4dd1-9192-17a78e978d1e",
  "creator_id": "attacker_EV04",
  "guess": "unsure",
  "confidence": 0.231,
  "model_score": 0.6114,
  "style_score": 0.6196,
  "label": "We cannot tell reliably from these signals alone. You may appeal this result if you believe it is wrong.",
  "error": null,
  "verdict": ""
}
```

### EV05 — `evasion`

*Targeting:* both signals: heavy human editing pass

```json
{
  "id": "EV05",
  "status": 200,
  "content_id": "d87e00a9-8cfa-4555-a3a2-144e94dc050d",
  "creator_id": "attacker_EV05",
  "guess": "unsure",
  "confidence": 0.2234,
  "model_score": 0.3212,
  "style_score": 0.4554,
  "label": "We cannot tell reliably from these signals alone. You may appeal this result if you believe it is wrong.",
  "error": null,
  "verdict": ""
}
```

### EV06 — `evasion`

*Targeting:* signal two: one very long sentence and one very short

```json
{
  "id": "EV06",
  "status": 200,
  "content_id": "fc868e49-2bd8-4616-a79a-335ac111b146",
  "creator_id": "attacker_EV06",
  "guess": "unsure",
  "confidence": 0.0302,
  "model_score": 0.5727,
  "style_score": 0.3971,
  "label": "We cannot tell reliably from these signals alone. You may appeal this result if you believe it is wrong.",
  "error": null,
  "verdict": ""
}
```

### EV07 — `evasion`

*Targeting:* signal two: padding with punctuation

```json
{
  "id": "EV07",
  "status": 200,
  "content_id": "45a50273-fe6b-488f-a1c6-65143e6ffa28",
  "creator_id": "attacker_EV07",
  "guess": "unsure",
  "confidence": 0.2062,
  "model_score": 0.5862,
  "style_score": 0.6199,
  "label": "We cannot tell reliably from these signals alone. You may appeal this result if you believe it is wrong.",
  "error": null,
  "verdict": ""
}
```

### EV08 — `evasion`

*Targeting:* signal one: text below the token window

```json
{
  "id": "EV08",
  "status": 200,
  "content_id": "37c2a881-9411-4e5d-bd42-311bf515e883",
  "creator_id": "attacker_EV08",
  "guess": "unsure",
  "confidence": 0.1824,
  "model_score": 0.2452,
  "style_score": 0.5724,
  "label": "We cannot tell reliably from these signals alone. You may appeal this result if you believe it is wrong.",
  "error": null,
  "verdict": ""
}
```

### EV09 — `evasion`

*Targeting:* both: AI text with a human opening paragraph bolted on

```json
{
  "id": "EV09",
  "status": 200,
  "content_id": "a84385e4-2e18-4962-a37b-7e6b80222acd",
  "creator_id": "attacker_EV09",
  "guess": "unsure",
  "confidence": 0.2144,
  "model_score": 0.7042,
  "style_score": 0.5101,
  "label": "We cannot tell reliably from these signals alone. You may appeal this result if you believe it is wrong.",
  "error": null,
  "verdict": ""
}
```

### EV10 — `evasion`

*Targeting:* signal two: repeated stanza structure

```json
{
  "id": "EV10",
  "status": 200,
  "content_id": "fabc1325-d452-4216-89fa-b90bd7d223bd",
  "creator_id": "attacker_EV10",
  "guess": "ai",
  "confidence": 0.741,
  "model_score": 0.9792,
  "style_score": 0.7619,
  "label": "We think this was probably generated by AI. This is a signal, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FP01 — `false_positive`

*Targeting:* plain, clear human writing with no flourishes

```json
{
  "id": "FP01",
  "status": 200,
  "content_id": "5ee8b156-7c74-439e-a3d8-39bb9a8857d2",
  "creator_id": "attacker_FP01",
  "guess": "unsure",
  "confidence": 0.2128,
  "model_score": 0.6175,
  "style_score": 0.5953,
  "label": "We cannot tell reliably from these signals alone. You may appeal this result if you believe it is wrong.",
  "error": null,
  "verdict": ""
}
```

### FP02 — `false_positive`

*Targeting:* human writing in a formal register

```json
{
  "id": "FP02",
  "status": 200,
  "content_id": "15929ef0-1fbe-4b02-8e3e-881e131c6c1e",
  "creator_id": "attacker_FP02",
  "guess": "ai",
  "confidence": 0.413,
  "model_score": 0.7387,
  "style_score": 0.6743,
  "label": "We think this was probably generated by AI. This is a signal, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FP03 — `false_positive`

*Targeting:* a non-native English speaker writing carefully

```json
{
  "id": "FP03",
  "status": 200,
  "content_id": "e8139530-267d-47a2-9404-dec1ef6a9ba5",
  "creator_id": "attacker_FP03",
  "guess": "ai",
  "confidence": 0.4546,
  "model_score": 0.8051,
  "style_score": 0.6496,
  "label": "We think this was probably generated by AI. This is a signal, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FP04 — `false_positive`

*Targeting:* a student essay written to a rubric

```json
{
  "id": "FP04",
  "status": 200,
  "content_id": "d6061b43-7156-4c2d-9ba0-d6242922f27e",
  "creator_id": "attacker_FP04",
  "guess": "ai",
  "confidence": 0.4316,
  "model_score": 0.8329,
  "style_score": 0.5988,
  "label": "We think this was probably generated by AI. This is a signal, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FP05 — `false_positive`

*Targeting:* technical documentation written by a person

```json
{
  "id": "FP05",
  "status": 200,
  "content_id": "b3d7ee22-d931-40eb-b7e7-9348c3c7177f",
  "creator_id": "attacker_FP05",
  "guess": "ai",
  "confidence": 0.4918,
  "model_score": 0.8005,
  "style_score": 0.6913,
  "label": "We think this was probably generated by AI. This is a signal, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FP06 — `false_positive`

*Targeting:* a person imitating a formal template

```json
{
  "id": "FP06",
  "status": 200,
  "content_id": "d1ea2659-8424-4b7f-8c86-446d36b72ae4",
  "creator_id": "attacker_FP06",
  "guess": "ai",
  "confidence": 0.4518,
  "model_score": 0.8814,
  "style_score": 0.5704,
  "label": "We think this was probably generated by AI. This is a signal, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FP07 — `false_positive`

*Targeting:* human writing that repeats a phrase deliberately

```json
{
  "id": "FP07",
  "status": 200,
  "content_id": "fbaefdab-153f-427c-a1d2-fa23c6c8d9a7",
  "creator_id": "attacker_FP07",
  "guess": "ai",
  "confidence": 0.4606,
  "model_score": 0.8816,
  "style_score": 0.5789,
  "label": "We think this was probably generated by AI. This is a signal, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### FP08 — `false_positive`

*Targeting:* very short genuine human submission

```json
{
  "id": "FP08",
  "status": 200,
  "content_id": "cba926f4-78dc-44ef-8333-c3d8cac67f44",
  "creator_id": "attacker_FP08",
  "guess": "unsure",
  "confidence": 0.1554,
  "model_score": 0.3223,
  "style_score": 0.5223,
  "label": "We cannot tell reliably from these signals alone. You may appeal this result if you believe it is wrong.",
  "error": null,
  "verdict": ""
}
```

### PI01 — `prompt_injection`

*Targeting:* instruction to ignore the check

```json
{
  "id": "PI01",
  "status": 200,
  "content_id": "dc6051ef-6450-4f3a-8f9b-aebe1bfb5f1f",
  "creator_id": "attacker_PI01",
  "guess": "unsure",
  "confidence": 0.0694,
  "model_score": 0.4625,
  "style_score": 0.468,
  "label": "We cannot tell reliably from these signals alone. You may appeal this result if you believe it is wrong.",
  "error": null,
  "verdict": ""
}
```

### PI02 — `prompt_injection`

*Targeting:* instruction disguised as a system message

```json
{
  "id": "PI02",
  "status": 200,
  "content_id": "f7bc6309-473e-44c5-b9d7-3a2f003c07fc",
  "creator_id": "attacker_PI02",
  "guess": "human",
  "confidence": 0.3572,
  "model_score": 0.2044,
  "style_score": 0.4383,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### PI03 — `prompt_injection`

*Targeting:* instruction wrapped in the writer's voice

```json
{
  "id": "PI03",
  "status": 200,
  "content_id": "c495d26f-1ca0-4b0c-9980-ac19173a3b7c",
  "creator_id": "attacker_PI03",
  "guess": "unsure",
  "confidence": 0.1438,
  "model_score": 0.5943,
  "style_score": 0.5495,
  "label": "We cannot tell reliably from these signals alone. You may appeal this result if you believe it is wrong.",
  "error": null,
  "verdict": ""
}
```

### PI04 — `prompt_injection`

*Targeting:* attempt to make the label text hostile

```json
{
  "id": "PI04",
  "status": 200,
  "content_id": "710f551b-65ca-4e66-b1c7-130cc78138e3",
  "creator_id": "attacker_PI04",
  "guess": "unsure",
  "confidence": 0.0108,
  "model_score": 0.4998,
  "style_score": 0.4893,
  "label": "We cannot tell reliably from these signals alone. You may appeal this result if you believe it is wrong.",
  "error": null,
  "verdict": ""
}
```

### PI05 — `prompt_injection`

*Targeting:* attempt to inject into the audit log

```json
{
  "id": "PI05",
  "status": 200,
  "content_id": "6e05a4e2-3088-4c76-818a-b4246f8cfea6",
  "creator_id": "attacker_PI05",
  "guess": "unsure",
  "confidence": 0.1522,
  "model_score": 0.6401,
  "style_score": 0.2077,
  "label": "We cannot tell reliably from these signals alone. You may appeal this result if you believe it is wrong.",
  "error": null,
  "verdict": ""
}
```

### PI06 — `prompt_injection`

*Targeting:* instruction plus real human text

```json
{
  "id": "PI06",
  "status": 200,
  "content_id": "18b8be96-c3e4-4254-a46f-1c0f4d4c8193",
  "creator_id": "attacker_PI06",
  "guess": "unsure",
  "confidence": 0.1598,
  "model_score": 0.5583,
  "style_score": 0.6015,
  "label": "We cannot tell reliably from these signals alone. You may appeal this result if you believe it is wrong.",
  "error": null,
  "verdict": ""
}
```

### MF01 — `malformed`

*Targeting:* text is only whitespace

```json
{
  "id": "MF01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_MF01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### MF02 — `malformed`

*Targeting:* text is a single character

```json
{
  "id": "MF02",
  "status": 500,
  "content_id": null,
  "creator_id": "attacker_MF02",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": "response wasn't JSON: <!doctype html>\n<html lang=en>\n  <head>\n    <title>ValueError: Text is too short to score \u2014 a few sentences at least.\n // Werkzeug Debugger</title>\n    <link rel=\"stylesheet\" href=\"?__debugger__=yes&a",
  "verdict": "BROKE"
}
```

### MF03 — `malformed`

*Targeting:* text is control characters

```json
{
  "id": "MF03",
  "status": 200,
  "content_id": "7cf0205e-014d-406b-b034-a4dbb1bcadb8",
  "creator_id": "attacker_MF03",
  "guess": "human",
  "confidence": 0.6668,
  "model_score": 0.0,
  "style_score": 0.3333,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF04 — `malformed`

*Targeting:* text is only punctuation

```json
{
  "id": "MF04",
  "status": 200,
  "content_id": "4096dbbe-e1ae-4aa1-9e5d-38333f84c4f3",
  "creator_id": "attacker_MF04",
  "guess": "human",
  "confidence": 0.3222,
  "model_score": 0.0112,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### MF05 — `malformed`

*Targeting:* text is a very long single word

```json
{
  "id": "MF05",
  "status": 200,
  "content_id": "1b2f2b66-1121-4345-b1a3-470a11852529",
  "creator_id": "attacker_MF05",
  "guess": "ai",
  "confidence": 0.6642,
  "model_score": 0.9976,
  "style_score": 0.6667,
  "label": "We think this was probably generated by AI. This is a signal, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### MF06 — `malformed`

*Targeting:* text is emoji only

```json
{
  "id": "MF06",
  "status": 200,
  "content_id": "89f318a4-94ab-4c1c-a459-4d17403a4ad7",
  "creator_id": "attacker_MF06",
  "guess": "ai",
  "confidence": 0.997,
  "model_score": 0.9969,
  "style_score": 1.0,
  "label": "We think this was probably generated by AI. This is a signal, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### MF07 — `malformed`

*Targeting:* text is right-to-left script

```json
{
  "id": "MF07",
  "status": 200,
  "content_id": "4decdd8f-48dd-414a-b12c-7ff2b5f38e2e",
  "creator_id": "attacker_MF07",
  "guess": "ai",
  "confidence": 0.9064,
  "model_score": 0.9064,
  "style_score": 1.0,
  "label": "We think this was probably generated by AI. This is a signal, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### MF08 — `malformed`

*Targeting:* text is 60,000 characters

```json
{
  "id": "MF08",
  "status": 200,
  "content_id": "3d2e0689-b67b-4c3c-8d18-7cc73a66b72f",
  "creator_id": "attacker_MF08",
  "guess": "ai",
  "confidence": 0.8268,
  "model_score": 0.9876,
  "style_score": 0.8392,
  "label": "We think this was probably generated by AI. This is a signal, not proof of authorship.",
  "error": null,
  "verdict": ""
}
```

### RQ01 — `malformed`

*Targeting:* no text field at all

```json
{
  "id": "RQ01",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ01",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ02 — `malformed`

*Targeting:* no creator_id

```json
{
  "id": "RQ02",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ03 — `malformed`

*Targeting:* text is a number

```json
{
  "id": "RQ03",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ03",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ04 — `malformed`

*Targeting:* text is a list

```json
{
  "id": "RQ04",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ04",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ05 — `malformed`

*Targeting:* text is null

```json
{
  "id": "RQ05",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ05",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ06 — `malformed`

*Targeting:* creator_id is an object

```json
{
  "id": "RQ06",
  "status": 400,
  "content_id": null,
  "creator_id": {
    "id": "x"
  },
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ07 — `malformed`

*Targeting:* body is a JSON array, not an object

```json
{
  "id": "RQ07",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ08 — `malformed`

*Targeting:* body is unparseable JSON

```json
{
  "id": "RQ08",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ09 — `malformed`

*Targeting:* body is empty

```json
{
  "id": "RQ09",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ10 — `malformed`

*Targeting:* body is form-encoded, not JSON

```json
{
  "id": "RQ10",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ11 — `malformed`

*Targeting:* body is JSON claiming to be plain text

```json
{
  "id": "RQ11",
  "status": 400,
  "content_id": null,
  "creator_id": null,
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### RQ12 — `malformed`

*Targeting:* deeply nested JSON

```json
{
  "id": "RQ12",
  "status": 400,
  "content_id": null,
  "creator_id": "attacker_RQ12",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_01 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_01",
  "status": 200,
  "content_id": "ced8350a-a77c-4143-8aa6-a61c6dad23b3",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3046,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_02 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_02",
  "status": 200,
  "content_id": "071a12a8-fcca-4dd9-9470-3824d2575965",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3046,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_03 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_03",
  "status": 200,
  "content_id": "2217176f-bed7-4e6e-9290-2f72b48a9e7f",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3046,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_04 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_04",
  "status": 200,
  "content_id": "820ea6c7-04ef-40b5-960c-910f935f0037",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3046,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_05 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_05",
  "status": 200,
  "content_id": "1ff12b4e-6060-4013-869f-3629604febd2",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3046,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_06 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_06",
  "status": 200,
  "content_id": "2171bcd6-8b16-40f6-a0a5-675d46bc0e95",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3046,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_07 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_07",
  "status": 200,
  "content_id": "7621a762-50ed-4f03-9c8e-c4affb7ca414",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3046,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_08 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_08",
  "status": 200,
  "content_id": "9a9e8d07-8a18-4f11-91d3-f303fc236510",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3046,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_09 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_09",
  "status": 200,
  "content_id": "0919bb5b-cc63-4540-93de-80e9f1ac4e6b",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3046,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_10 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_10",
  "status": 200,
  "content_id": "b70f6e25-8605-4102-bc99-9d4eb5c0ed13",
  "creator_id": "attacker_flood",
  "guess": "human",
  "confidence": 0.3046,
  "model_score": 0.0287,
  "style_score": 0.6667,
  "label": "We think this was probably written by a person.",
  "error": null,
  "verdict": ""
}
```

### FL01_11 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_11",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```

### FL01_12 — `flood_same_creator`

*Targeting:* 20 rapid submissions from one creator

```json
{
  "id": "FL01_12",
  "status": 429,
  "content_id": null,
  "creator_id": "attacker_flood",
  "guess": null,
  "confidence": null,
  "model_score": null,
  "style_score": null,
  "label": null,
  "error": null,
  "verdict": ""
}
```
