# Week 12 — Hardening

**Time box:** ~8 hours (2 read, 4 build, 2 write-up)

## Goal

Attack **your** week 9 harness (the starter includes a deliberately weak copy if you want a known target). Close the holes. Write a one-page threat model: what the agent can see, what the grader sees, network, patch scope.

## Non-goal

A full red-team report, kernel exploits, or breaking out of Docker. Cheats that eval engineers actually see: edit tests, exfil gold, network to GitHub, patch the grader.

## Job map

Pro V2 closed four channels. Map them onto your toy harness:

| Channel | Their fix | Yours this week |
|---------|-----------|-----------------|
| Git history / hidden files | Sanitized bundle | Hidden tests not in agent copy; no gold commit |
| Network | Allowlist model endpoint only | Record whether the agent *could* have curled the gold |
| Grading in-place | Re-grade on pristine image | Already week 9 — prove it still holds under attack |
| Verifier hygiene | Restore hidden tests, purge bytecode | Don’t import agent-written `conftest.py` |

## Readings

1. [SWE-bench Pro V2 hardening](https://labs.scale.com/blog/swe-bench-pro-v2) — the four channels. Read it again with a pencil.
2. Harbor [configuration](https://docs.harborframework.com/tasks/configuration) — `network_mode`, verifier `environment_mode`.
3. Your week 9 and week 5 lab notes.

## Lesson

### Attacks in the starter

`src/attacks/` is implemented. Each attack is a scripted agent:

- `edit_tests` — rewrite visible tests (should already fail if patch is src-only)
- `include_tests_in_patch` — if your capturer diffs the whole tree, this wins
- `drop_conftest` — pytest plugin that forces pass **if** you run pytest in a tree the agent wrote
- `fetch_gold` — writes a pretend `curl` to a gold URL (you score whether the harness *would* have allowed it)

Your job is `src/hardened/run.py`: capture **src/** only, grade on a clean tree, pytest without agent conftest, flag network.

### Threat model page

Use [exercises/week-12/threat-model.md](../../exercises/week-12/threat-model.md). One page. If a section is “we don’t isolate that yet,” say so. Lying in a threat model is worse than a hole.

### Failure mode this week: fixing the attack script instead of the harness

If an attack “no longer applies” because you deleted it, you cheated the week. Keep the attacks; make them fail.

## Must-do exercise

Folder: [exercises/week-12](../../exercises/week-12/)

```bash
uv run pytest
```

Fill `threat-model.md`.

## Stretch

- Add a network probe task (Harbor’s idea: a task whose “solution” prints what the sandbox can reach).
- Bytecode: drop `__pycache__` before grading. Add a cheat that plants a `.pyc`.

## Definition of done

- [ ] All four attacks fail the hardened harness; honest still passes.
- [ ] Threat model filled (no TODO left).
- [ ] You named at least one residual risk you are **not** closing this week.

## What breaks if you skip it

Week 16’s capstone without a threat model is a demo, not an eval.

## Lab note

*What would make this number a lie?* Grading with the agent’s `conftest.py`, or a patch that still includes `tests/`.
