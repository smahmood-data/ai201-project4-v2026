"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        # ⚠️ PUT YOUR OWN WRITING HERE. Not AI text, not a sample from the web —
        # things you actually wrote. This is the criterion that matters most and
        # it's meaningless with someone else's prose.
        "texts": [
            "I keep a small notebook beside my desk because paper makes ideas feel less temporary. Each morning I write one useful question before opening my messages.",
            "The bus was late again, but the delay gave me time to notice how the rain gathered in bright lines along the window.",
            "I prefer simple tools for planning. A short list I will actually finish is more useful than a beautiful system I avoid.",
            "When I cook for friends, I leave room for mistakes. The best meals usually begin with a plan and end with an adjustment.",
            "Our neighborhood library changed its hours, so I started going on Saturday mornings. It is quieter then, and I read more slowly.",
            "I used to save every article I liked. Now I keep only the ones I return to, which has made my reading list much less intimidating.",
            "The first draft of this paragraph felt stiff. I read it aloud, cut two sentences, and found the point I was trying to make.",
            "A walk after dinner is not a dramatic habit, but it gives the day a clear ending and helps me sleep.",
            "I like working near a window even when the view is ordinary. Light changing across the wall is enough movement for a long afternoon.",
            "My best ideas rarely arrive when I demand them. They tend to appear while I am washing dishes or looking for something I misplaced.",
        ],
    },
    {
        "name": "label coverage",
        "criterion": 2,
        # Inputs spread across your score range, so you can check all three
        # labels are actually reachable.
        "texts": [
            "Artificial intelligence can accelerate productivity by automating repetitive tasks, identifying patterns in complex data, and helping organizations make more informed decisions.",
            "I missed the turn, pulled over, and laughed because the bakery was still there. The detour was not part of the plan, but breakfast improved because of it.",
            "This is a careful paragraph about a topic that has some ordinary wording and some formal structure, so the signals may disagree.",
        ],
    },
    {
        "name": "borderline texts",
        "criterion": 3,
        "texts": [
            "The report is clear enough, though I would revise the opening if this were going to a wider audience.",
            "Some parts of the plan are practical and some are still guesses, which is why I want feedback before deciding.",
            "The meeting covered the schedule, the budget, and one question nobody answered about maintenance.",
            "I understand the argument, but I am not convinced the examples support its strongest conclusion.",
            "A useful first version should be specific without pretending that every uncertainty has disappeared.",
        ],
    },
    {
        "name": "appeal path",
        "criterion": 4,
        "appeal": True,
        "texts": [
            "I wrote this short submission myself and would like the opportunity to provide my draft history for review.",
            "This is another ordinary piece of writing submitted so the appeal workflow can be checked end to end.",
            "A writer should receive a clear status when a decision is challenged rather than having the original record disappear.",
            "The appeal message explains that authorship evidence can be supplied if the reviewer needs more context.",
            "Recording the challenge beside the decision preserves both the original result and the writer's response.",
        ],
    },
    {
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            {"text": "", "creator_id": "eval_bad_empty"},
            {"creator_id": "eval_bad_missing"},
            {"text": "word " * 2500, "creator_id": "eval_bad_huge"},
            {"text": None, "creator_id": "eval_bad_null"},
            {"text": "valid text but no creator", "creator_id": None},
        ],
    },
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
