# Week 16 — Capstone

**Time box:** ~8 hours (2 read, 4 build, 2 write-up) — the report may spill into a second sitting. That is fine. The **artifact** is the report plus a runnable suite, not a slide deck.

## Goal

A private **10-task** gauntlet, hidden tests, oracle sanity check, baseline + **one** hill-climb with paired comparison and a CI, written report: what you measured, what leaked, what you changed, what you still don’t trust.

This is the interview artifact.

## Non-goal

SOTA on a public leaderboard. A Next.js LMS. Perfect scores.

## Job map

The week 16 bar from the README:

> Author a Harbor-format task, explain why a trusting harness is worthless, grade a patch on a clean environment, classify failures into repair surfaces, run a frozen gauntlet, change one lever, and defend the before/after number (n, CI, holdouts).

## Readings

1. Your own lab notes from weeks 5, 7, 8, 12, 14.
2. The capstone template: [exercises/week-16/capstone-report.md](../../exercises/week-16/capstone-report.md)

No new blog posts. If you need a new source to finish the report, the eval is not frozen.

## Lesson

### Ten tasks

Reuse week 13’s five. Add five you authored (Harbor-shaped or week 9-shaped). At least two must be unit-test style, at least one terminal. Oracle 10/10 before any agent comparison.

### Holdout

Two of the ten are **holdout**: you may not look at their traces while choosing the hill-climb lever. Score them after you lock the candidate. If holdout collapses, say so — that is a good report.

### One hill-climb

Exactly one lever, paired on the eight non-holdout tasks, CI from week 7 (bootstrap on the 0/1 vector). Keep or revert. Then score holdout.

### Failure mode this week: a beautiful report of an untrusted harness

If you still grade in-place, the rest is fiction. Re-run week 12 attacks on the capstone harness; paste the table.

## Must-do exercise

Folder: [exercises/week-16](../../exercises/week-16/)

- Checklist in `README.md`
- Report template you fill (`capstone-report.md` is the submitted artifact; keep a private copy if you want)
- `suite/` with five new task stubs plus pointers to week 13

You do not need a new Python package if you compose week 9 + 13 runners. You do need the report.

## Stretch

- Inspect or Harbor CLI on the ten tasks.
- A one-page threat model (week 12) attached as appendix.

## Definition of done

- [ ] Oracle 10/10.
- [ ] Week 12 attacks fail on this harness (table in the report).
- [ ] Baseline vs one candidate, paired, bootstrap CI, keep/revert.
- [ ] Holdout scored after lock.
- [ ] Report names residual risks and at least one number you **refuse** to quote publicly.
- [ ] No Next.js, no extra scope.

## What breaks if you skip it

Without this artifact, the curriculum was a reading list. With it, you can defend the job.

## Lab note

*What would make this number a lie?* Everything you have practiced. List the top three for *this* suite in the report’s last section.
