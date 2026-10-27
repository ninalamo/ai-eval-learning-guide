# Week 7 — Statistics that keep you honest

**Time box:** ~8 hours (2 read, 4 build, 2 write-up)

## Goal

Simulate a noisy agent and prove to yourself that **n=3 can show a fake win**. Implement pass rates, a bootstrap confidence interval, and a paired comparison. No new eval framework.

## Non-goal

Deriving the CLT, publishing a paper, or installing a Bayesian stack. Bootstrap + “do not claim a 3-point gain on five tasks” is the bar.

## Job map

| Claim you want to make | Evidence this week demands |
|------------------------|----------------------------|
| “Candidate is better” | Same tasks, paired, CIs that do not fully overlap *or* a pre-registered delta with enough n |
| “Pass@1 is 80%” | n tasks, interval, not a point |
| “It is stable” | Repeated trials / pass@k, not one lucky run |

## Readings

1. [Inspect evaluation metrics — reduction](https://inspect.aisi.org.uk/eval-metrics.html) — how epochs/reducers turn trials into a number. Skim.
2. Glossary: [pass@k](../glossary.md), [CI](../glossary.md), [paired comparison](../glossary.md).
3. Optional: any short note on bootstrap percentile intervals (your choice of source). You will implement 1,000 resamples; you do not need a library.

## Lesson

### Agents are coins with unknown p

A task-level pass is roughly Bernoulli. Five flips of a p=0.5 coin can easily land 4/5. The next candidate, also p=0.5, can land 2/5. You will “ship” the first one if you do not look at n.

The simulator draws `passed ~ Bernoulli(p)` per task. Baseline and candidate can share the **same** latent `p` so a “win” is false by construction. That is the pedagogical knife.

### Bootstrap CI (percentile)

1. You have a list of 0/1 per task.
2. Resample that list with replacement, same length, `B` times (1000).
3. Each resample has a mean. Sort the means. 2.5th and 97.5th percentiles are the 95% interval.

If the interval for n=3 is `[0.0, 1.0]`, you may not quote 0.67 as a capability.

### Pairing

Improvement is `candidate - baseline` **per task**, then mean of deltas. Comparing 8 random tasks on A to 8 other tasks on B is how dashboards lie. The exercise locks pairing.

### Failure mode this week: p-hacking the gauntlet

Re-running the candidate until n=3 looks better, then stopping. The loop in week 14 forbids this: freeze seeds and trial counts **before** looking. This week, the simulator accepts a seed so you can reproduce a false win on demand.

## Must-do exercise

Folder: [exercises/week-07](../../exercises/week-07/)

Implement `simulate`, `pass_rate`, `bootstrap_ci`, `paired_delta`, and `false_win_n3` as specified by the tests.

Run `uv run python -m stats_sim` and paste the n=3 vs n=100 table into the lab note.

## Stretch

- Implement pass@k by simulating k trials per task.
- Plot nothing — print a text histogram of bootstrap means. If you need a chart, it is optional and not the deliverable.

## Definition of done

- [ ] Tests green.
- [ ] You have a reproduced false win: same true p, n=3, candidate point estimate higher, CIs overlapping.
- [ ] n=100 on the same p: CIs overlap and you would **not** ship.
- [ ] Paired delta is computed per-task, not as `mean(A) - mean(B)` on shuffled ids.

## What breaks if you skip it

Week 16’s capstone requires a CI and a paired comparison. Without this week you will write “we improved 12%” on ten noisy tasks and fail the interview.

## Lab note

*What would make this number a lie?* n=3, no interval, unpaired tasks, or re-rolling the candidate until the delta is positive.
