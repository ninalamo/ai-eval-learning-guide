# Week 8 — Failure taxonomy

**Time box:** ~8 hours (2 read, 4 build, 2 write-up)

## Goal

Label eight synthetic traces so that each label maps to a **repair surface**. Catch-all buckets fail the week. You are practicing the diagnosis step of the gauntlet loop before the loop exists.

## Non-goal

Building a classifier model. Auto-labeling production at scale. A 40-class ontology copied from a blog.

## Job map

A useful row has three fields, not one:

| Field | Question | Example |
|-------|----------|---------|
| Symptom | What did you observe? | `wrong_tool`, `timeout`, `tests_failed` |
| Suspected cause | Why, as a hypothesis? | `ambiguous_tool_description` |
| Repair surface | What would you change **one of**? | `tool_contract`, `prompt`, `harness`, `grader`, `task`, `environment`, `model_ceiling` |

If two labels always lead to the same fix, they are one label.

## Readings

1. [Agent improvement loops — failure taxonomies](https://exalted-ai.com/blog/agent-improvement-loops) — symptom vs cause vs repair surface. Read that distinction; skip the rest if short on time.
2. Glossary: [failure taxonomy](../glossary.md), [repair surface](../glossary.md).
3. Optional: [METR — algorithmic vs holistic evaluation](https://metr.org/blog/2025-08-12-research-update-towards-reconciling-slowdown-with-time-horizons/) — even passing tests can fail a human review. One trace this week is that case.

## Lesson

### Allowed repair surfaces (closed set)

Use **only** these for `repair_surface` so we can compare notes later:

- `prompt` — system/instruction scaffolding, not the task instruction
- `tool_contract` — names, descriptions, args, error strings
- `harness` — isolation, timeouts, missing files in the sandbox
- `grader` — scorer is wrong or too strict; agent actually solved it
- `task` — instruction ambiguous or gold wrong
- `environment` — image, packages, network
- `model_ceiling` — you would not expect this model to do it; changing prompt is theater

`misc` / `other` / `needs_investigation` are **not** allowed in the must-do answers. If you are unsure, pick the best surface and write the doubt in `notes`.

### One mutation per trace

`proposed_mutation` is a single sentence: “Rewrite the `run_tests` tool description to say it is required before `submit`.” Not “improve prompting and maybe switch models.”

### Failure mode this week: labeling the fix you already wanted

If every trace comes out `prompt`, you are not reading traces. Trace 07 is a grader bug on purpose. Trace 08 is model ceiling. If you mark those as `prompt`, re-read.

## Must-do exercise

Folder: [exercises/week-08](../../exercises/week-08/)

1. Read `data/traces/01.json` … `08.json`.
2. Fill `answers.json` (copy from `answers.template.json`).
3. `uv run python -m taxonomy check` — schema and closed-set surfaces. This does **not** grade correctness.
4. After you lock answers, `uv run python -m taxonomy grade` compares to `data/gold-answers.json`. You may disagree; if you do, write why in `notes`. Gold is a senior’s take, not physics.

## Stretch

- Merge two traces that share a surface into a gauntlet ticket: “If I change X, I expect traces {i,j} to flip.”
- Add a ninth trace from a real Cursor session (redact secrets) and label it.

## Definition of done

- [ ] Eight answers, all required fields, only allowed surfaces.
- [ ] No `other` / `misc`.
- [ ] Trace 07 is not labeled `prompt` unless your notes explain a genuine prompt-only fix that would beat a grader bug (it will not).
- [ ] Trace 08 is `model_ceiling` or you wrote a strong rebuttal.
- [ ] You ran `taxonomy grade` and recorded matches vs gold in the lab note.

## What breaks if you skip it

Week 14 says “mutate one lever.” Without a taxonomy you will mutate the prompt every time, which is how teams spend a quarter on a plateau.

## Lab note

*What would make this number a lie?* A taxonomy nobody applies twice the same way, or labels that describe the fix you wanted to make before you opened the trace.
