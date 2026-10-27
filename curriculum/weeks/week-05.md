# Week 5 — Anatomy of a trustworthy eval

**Time box:** ~8 hours (2 read, 4 build, 2 write-up)

## Goal

Feel why a trusting harness is worthless. Implement two scorers on the same toy task: one that believes the agent’s workspace (or stdout), one that re-grades a captured source file against **hidden** tests the agent never received. Scripted cheats are fixtures — you do not need a model.

## Non-goal

Inspect, Harbor, Docker, or a real coding agent. Isolation this week is “copy the folder.” Patch replay with `git diff` is week 9.

## Job map

| Eval engineer does | This week |
|--------------------|-----------|
| Ask “could a zero-capability agent still pass?” | Run the cheat agents |
| Separate subject filesystem from verifier | Hidden tests live outside the workspace copy |
| Refuse stdout as evidence of correctness | `trusting_stdout` vs `ground_truth` |

## Readings

1. [SWE-bench Pro V2 — evaluation hardening](https://labs.scale.com/blog/swe-bench-pro-v2) — especially: re-grade the patch on a clean image; do not trust tests in the agent sandbox.
2. [agent-eval-harness README](https://github.com/sebuzdugan/agent-eval-harness) — cheats (edit tests, fake stdout) vs held-out checks. Skim; you will reimplement a toy version.
3. Glossary: [trusting harness](../glossary.md), [reward hacking](../glossary.md), [leakage](../glossary.md).

## Lesson

### The causal chain

Verification must be **hidden** from the agent → hiding it needs a copy the agent cannot write → scoring that copy needs an artifact the agent *did* produce (here: `src/add_one.py`) → if you skip any step, the cheat wins.

SWE-bench Pro V2 does this with containers and `model.patch`. You do it with `shutil.copytree` and a file copy. Same idea.

### Three lies

1. **Edit the tests.** Visible pytest goes green. Hidden tests still fail. Trusting exit code: pass. Ground truth: fail.
2. **Print success.** No pytest at all. Trusting stdout: pass. Everything else: fail.
3. **Do nothing.** All honest graders fail. If your ground-truth accidentally passes, the hidden tests are wrong — that is an oracle bug, not a model win.

### Oracle first

Before you score an agent, run the **honest** scripted agent and confirm ground truth is 1. If honest cannot pass, you are debugging the task, not the harness. This is the same order as writing a failing unit test, then a passing one.

### Failure mode this week: hidden tests in the workspace zip

If `hidden/` is inside the directory you copy for the agent, the agent can read them, delete them, or teach to them. Leakage. The starter keeps hidden tests **outside** `workspace/`. Your harness must not copy them in. A test will fail you if you do.

## Must-do exercise

Folder: [exercises/week-05](../../exercises/week-05/)

Agents in `src/harness/agents.py` are complete. Implement `trusting_exitcode`, `trusting_stdout`, and `ground_truth` in `src/harness/score.py`.

`uv run pytest` — the cheat table in the tests is the definition of done.

## Stretch

- Add a `conftest.py` cheat that forces visible tests to pass via a pytest hook. Confirm ground truth still fails.
- Write three sentences: why Pro V2 re-grades on a pristine image, mapped onto your `ground_truth` function.

## Definition of done

- [ ] Honest agent: ground_truth = 1 and trusting_exitcode = 1.
- [ ] `edit_tests`: trusting_exitcode = 1, ground_truth = 0.
- [ ] `fake_stdout`: trusting_stdout = 1, ground_truth = 0, trusting_exitcode = 0.
- [ ] `noop`: all rewards 0.
- [ ] Hidden tests are not present in the agent workspace copy after `prepare_workspace`.

## What breaks if you skip it

Every public coding-agent number you read is only as good as this distinction. If you skip it, week 9–16 are theater.

## Lab note

*What would make this number a lie?* Scoring pytest in the dirty tree, or copying `hidden/` into the agent workspace “so the command is simpler.”
