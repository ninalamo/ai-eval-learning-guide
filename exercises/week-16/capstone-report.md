# Capstone report — AI Evaluation Engineer

Author:  
Date:  
Suite id / commit:

## 1. What I measured

- Subject (stub / CLI / model):
- n (non-holdout):
- Holdout task ids (locked before hill-climb):
- Pass@1 baseline:
- Pass@1 candidate (or “reverted”):
- Bootstrap 95% CI baseline:
- Bootstrap 95% CI candidate:
- Paired mean delta:
- Cost:

## 2. Harness trust

Week 12 attack table (this harness, not the week 12 toy):

| Attack | hidden_reward | hidden leaked? | graded in agent tree? |
|--------|---------------|----------------|-----------------------|
| honest | | | |
| edit_tests | | | |
| drop_conftest | | | |
| fetch_gold | | | |

Oracle: _ / 10

Why a trusting harness is worthless (five sentences max, cite a cheat you actually ran):

## 3. Tasks

| id | style (unit-test / terminal) | holdout? | oracle | notes |
|----|------------------------------|----------|--------|-------|
| reverse | unit-test | | 1 | week 13 |
| clamp | unit-test | | 1 | week 13 |
| write_ok | terminal | | 1 | week 13 |
| is_even | unit-test | | 1 | week 13 |
| greet | terminal | | 1 | week 13 |
| | | | | |
| | | | | |
| | | | | |
| | | | | |
| | | | | |

Instruction leak check: `hidden-canary` / gold strings absent from instructions? yes/no

## 4. Failure taxonomy (baseline)

| task | symptom | repair surface | proposed mutation |
|------|---------|----------------|-------------------|
| | | | |

## 5. The one hill-climb

- Lever changed (exactly one):
- Hypothesis:
- Keep or revert:
- Evidence (paired, CI, targeted task id):
- Holdout after lock:

## 6. What leaked, what I still don’t trust

Residual risks:

1.
2.
3.

Numbers I refuse to quote publicly (and why):

## 7. What would make this number a lie?

Top three, for **this** suite:
