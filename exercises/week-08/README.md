# Week 8 exercise — label eight traces

1. Copy `answers.template.json` to `answers.json`.
2. Read `data/traces/*.json`.
3. Fill every object. `repair_surface` must be one of the closed set in the week lesson.
4. `uv run python -m taxonomy check`
5. After you would defend the labels: `uv run python -m taxonomy grade`

`grade` compares to `data/gold-answers.json`. Disagreement is allowed if `notes` explains it. Trace 07 must not be `prompt`; trace 08 must be `model_ceiling` unless you rebut in notes.
