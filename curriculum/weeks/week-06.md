# Week 6 — Graders

**Time box:** ~8 hours (2 read, 4 build, 2 write-up)

## Goal

Score the same five tasks with three graders (exact, schema, judge) and publish **disagreement**, not a single blended score. Calibrate the judge against a tiny human label column that is already in the file.

## Non-goal

Training a judge model, RAGAS, or “LLM-as-judge as a service.” The judge in the starter can be a rubric function; a live model is stretch.

## Job map

| Grader | Use when | Fails when |
|--------|----------|------------|
| Exact / unit tests | Closed answer, file bytes, test suite | Paraphrase, formatting, equivalent code |
| Schema | Structured output, tool args | Content is well-formed but wrong |
| Trajectory | Process matters (must call `read_file`) | Right outcome, forbidden path — or the reverse |
| LLM-as-judge | Open-ended quality | Judge drift, same-model narcissism, uncalibrated rubric |

## Readings

1. [Inspect scorers](https://inspect.aisi.org.uk/scorers.html) — how a serious framework talks about scoring. Skim the kinds; do not install Inspect until week 10.
2. [Pydantic Evals — evaluators](https://ai.pydantic.dev/evals/) — code-first evaluators. Optional; the idea is “grader is a function,” not a website.
3. Glossary: [grader](../glossary.md), [subject vs judge](../glossary.md).

## Lesson

### One number is a product decision, not a measurement

Product can ship a dashboard with a single “quality.” You must still keep the raw grader columns. When exact says 0 and judge says 1, that is a finding: either the gold is too brittle or the judge is too kind. Blending them into 0.7 hides the finding.

### Calibrate or do not quote

The five-task file includes `human_pass` (0/1) for the judge-relevant rows. Your judge’s accuracy vs human is a number you report. If you skip that, you are grading with an untested intern.

A **FakeJudge** that keys off keywords is allowed this week so tests stay offline. Document that it is a stub. Stretch: swap in Azure OpenAI and recompute agreement.

### Trajectory is not outcome

Task 3 requires calling `read_file` before answering. An agent that guesses the answer without the tool should fail the trajectory grader and might pass exact. That disagreement is the point: you choose which contract you are hiring the agent for.

### Failure mode this week: judge = subject

Scoring GPT-x with GPT-x on style will reward fluency. If you use a live judge, name the judge model in the report and keep it distinct from the subject. The starter’s FakeJudge is a different code path — good. Do not “improve” it by calling the same completer you would evaluate in week 4.

## Must-do exercise

Folder: [exercises/week-06](../../exercises/week-06/)

1. Implement `exact`, `schema`, `trajectory`, `judge` graders.
2. Implement `disagreement_report` — rows where graders do not all match `human_pass` or each other.
3. `uv run pytest` and `uv run python -m graders data/tasks.json`.

## Stretch

- Replace FakeJudge with a live Azure call; freeze the rubric in `rubric.md`.
- Add a fourth grader: JSON-schema via a real schema library. Compare to the key-set checker.

## Definition of done

- [ ] All three (plus trajectory) graders run on all five tasks without a network.
- [ ] Printed report includes per-grader pass rate **and** a disagreement table.
- [ ] Judge accuracy vs `human_pass` is computed (even if the judge is fake).
- [ ] You can name one task where exact and judge disagree and say which you would ship.

## What breaks if you skip it

Week 14 hill-climbs a metric. If you only have a vibe judge, you will keep prompt changes that please the judge and break tests.

## Lab note

*What would make this number a lie?* Averaging grader rewards into one “score” and quoting it as pass rate, or a judge that has never been compared to a human column.
