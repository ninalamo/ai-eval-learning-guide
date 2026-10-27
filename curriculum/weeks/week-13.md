# Week 13 — Run a public (or local) slice

**Time box:** ~8 hours (2 read, 4 build, 2 write-up)

## Goal

Run a **frozen five-task** suite twice (cheap stub vs slightly stronger stub, or cheap vs live model). Produce a run report: pass rate, cost, timeouts, failure list. Full SWE-bench / Terminal-Bench leaderboards are out of scope.

## Non-goal

Publishing a number. Tuning the agent until the slice is green. That is week 14, and it requires this report as the baseline.

## Job map

| Field | Why it is in the report |
|-------|-------------------------|
| Suite id + commit | If the tasks move, the number is incomparable |
| Agent / model / prompt hash | The subject |
| n, pass@1, timeouts | The headline with its scars |
| Cost (USD or tokens) | Cheap stubs cost 0; live models do not |
| Failures with trace ids | Input to week 8 taxonomy |
| Mock vs live | Week 10’s lie, again |

## Readings

1. [Inspect Harbor — SWE-bench Verified](https://meridianlabs-ai.github.io/inspect_harbor/registry/swe_bench_verified.html) — see how a *real* slice is invoked. Do not run 500 samples.
2. [Harbor cookbook](https://github.com/laude-institute/harbor) — optional; know it exists.
3. Your week 7 false-win table. You will be tempted to ignore it.

## Lesson

### Use the local slice unless you have budget

[exercises/week-13/suite](../../exercises/week-13/suite) is five Harbor-shaped tasks with oracles. Run them with the provided runner. That is a valid week 13.

A public slice is stretch: 5 Terminal-Bench or Inspect Harbor tasks, one cheap model, stop. Record cost. If a run will exceed a number you would not expense, do not start it.

### Freeze before you run

Write the suite list into the report **before** looking at scores. Changing the five tasks after seeing results is p-hacking (week 7).

### Failure mode this week: averaging two models in one table without pairing

Same five tasks, two subjects, two rows. Not “I swapped a task because it was flaky.” If a task is broken (oracle fails), drop it from **both** rows and say so.

## Must-do exercise

Folder: [exercises/week-13](../../exercises/week-13/)

```bash
uv run pytest
uv run python -m slice_runner --agent honest
uv run python -m slice_runner --agent weak
```

Fill [run-report.md](../../exercises/week-13/run-report.md).

## Stretch

- Five public Harbor/Inspect tasks on a cheap Azure deployment. Paste cost.
- Bootstrap CI on the five 0/1 scores (week 7). It will be wide. That is the lesson.

## Definition of done

- [ ] Report has suite identity, two subjects, pass@1, failure ids, mock-vs-live, cost.
- [ ] Oracle (honest) is 5/5 — if not, you are debugging tasks, not agents.
- [ ] Weak agent is not 5/5 (the slice has discriminative power).
- [ ] You did not drop a failing task only on the weak row.

## What breaks if you skip it

Week 14 has nothing to freeze. Week 16 has nothing to cite as a baseline.

## Lab note

*What would make this number a lie?* Unfrozen tasks, honest ≠ 5/5, or a live model quoted as if it were the stub.
