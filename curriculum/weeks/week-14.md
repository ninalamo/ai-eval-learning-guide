# Week 14 — The gauntlet loop

**Time box:** ~8 hours (2 read, 4 build, 2 write-up)

## Goal

Two full iterations on a frozen suite: diagnose from traces, mutate **one** lever, rerun, keep or revert. Log every experiment. Bundled changes fail the week.

## Non-goal

Autonomous “meta-agents” that rewrite the workspace unattended. You are the loop. Scripts only run trials.

## Job map

```text
freeze suite → run trials → score → taxonomy from traces
  → change one lever → rerun same suite → keep or revert
```

Levers allowed here: `system_prompt` (a string in `configs/`), `timeout_sec`, `tool_description`. Not “new model + new prompt + new tasks.”

## Readings

1. [cgraves09/gauntlet — the loop](https://github.com/cgraves09/gauntlet) — run, score, diagnose, mutate one thing, rerun. Skim the diagram.
2. [Hill climbing playbook](https://github.com/limecloud/agentqc/blob/main/docs/en/authoring/benchmark-and-hill-climbing.md) — freeze, one variable, noise, keep or revert, promote the failure into the suite.
3. Week 8 taxonomy. You will use those surfaces.

## Lesson

### Freeze

`suite.lock.json` lists task ids. Do not edit it during the two iterations. Configs live in `configs/baseline.json` and `configs/candidate.json`. Candidate starts as a copy of baseline; you change **one key**.

### Hypothesis is falsifiable

Bad: “improve the prompt.”  
Good: “`timeout` class is caused by 5s wall; raising to 30s should flip task `slow_install` and must not drop `reverse`.”

If the targeted task does not move, **revert** even if some other task improved. That other task is a confounder.

### Notebook

[lab-notebook.md](../../exercises/week-14/lab-notebook.md) has two iteration templates. Git history of `configs/` is the experiment log if you commit locally; the notebook is the narrative.

### Failure mode this week: changing the suite because the candidate looked bad

That is not a gauntlet. That is curriculum design. If a task is unfair, file it as `repair_surface: task` and leave it in the freeze until week 16 holdout policy.

## Must-do exercise

Folder: [exercises/week-14](../../exercises/week-14/)

The runner and a noisy scripted agent are provided. You:

1. Run baseline. Record scores.
2. Label failures (taxonomy).
3. Edit **one** field in `configs/candidate.json`.
4. Run candidate. Keep or revert. Write iteration 1.
5. Repeat for iteration 2 (if you reverted, pick a different lever).

`uv run python -m gauntlet run --config configs/baseline.json`

## Stretch

- Third iteration on a **holdout** task not in `suite.lock.json`. If holdout drops, you overfit.
- Pair with week 7 CI on the five scores.

## Definition of done

- [ ] Two notebook iterations, each with exactly one mutated key (diff the JSONs).
- [ ] Each iteration has a keep/revert decision and a reason that cites a task id.
- [ ] `suite.lock.json` unchanged.
- [ ] You did not edit the scripted agent’s hidden `p` to fake a win (that parameter is in `agents.py` comments — leave it).

## What breaks if you skip it

The capstone *is* this loop with more tasks. If you only ever ran a baseline, you cannot claim you can hill-climb.

## Lab note

*What would make this number a lie?* Two levers in one candidate, or a suite edit between baseline and candidate.
