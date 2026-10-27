# Week 16 — capstone checklist

The submitted artifact is `capstone-report.md` plus a runnable 10-task suite.

## Suite

- Five tasks: reuse [week 13](../week-13/suite) (`reverse`, `clamp`, `write_ok`, `is_even`, `greet`).
- Five new tasks: stubs under `suite/` in this folder. Finish them (instruction, workspace, hidden tests, oracle).
- Mark two of the ten as holdout in the report **before** the hill-climb.

## Harness

Compose week 9 / 12 / 13. Do not grade in the agent tree. Re-run week 12 attacks; paste the table.

## Loop

1. Oracle 10/10.
2. Baseline on the eight non-holdout tasks.
3. One lever. Paired comparison + bootstrap CI (week 7).
4. Keep or revert.
5. Score holdout after lock.

## Report

Fill every section of `capstone-report.md`. A section that does not apply still needs a sentence saying why.

```bash
# example, after you wire a runner
uv run pytest   # if you add tests for your five new oracles
```
