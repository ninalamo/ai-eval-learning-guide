# Week 9 — Mini-harness from scratch

**Time box:** ~8 hours (2 read, 4 build, 2 write-up)

## Goal

Build a tiny coding-agent harness: isolate a git workspace per task, run a **scripted** agent, capture `git diff`, apply that patch on a **clean** copy, run hidden tests. Three toy tasks. Honest agent passes; cheats fail.

## Non-goal

Inspect, Harbor CLI, Docker, or a live model. If you reach for an LLM, you are doing a different week.

## Job map

This is week 5 with two upgrades that match SWE-bench-style evals:

1. The artifact is a **patch**, not “whatever file we remembered to copy.”
2. The suite is **three tasks** with one runner, not a one-off function.

## Readings

1. [SWE-bench Pro V2 locked protocol](https://labs.scale.com/blog/swe-bench-pro-v2) — capture the diff; re-grade on a pristine image. You emulate this with `git diff` + a second checkout.
2. [Harbor task overview](https://docs.harborframework.com/tasks/overview) — instruction / environment / tests as a directory. Your `suite/<task>/` folders are a baby version.
3. Re-read your week 5 lab note. If trusting_exitcode still feels “good enough,” do not start this week.

## Lesson

### Isolation

```text
template  --copytree-->  agent_ws (git init, commit baseline)
agent mutates agent_ws
git diff > model.patch
template  --copytree-->  grade_ws (git init, commit baseline)
git apply model.patch in grade_ws
pytest hidden tests in grade_ws
```

Never run hidden tests in `agent_ws`. Never leave hidden tests inside the template the agent receives.

### What belongs in the patch

If the agent can diff `tests/`, it can delete assertions and the replay will apply that too. Restrict the captured paths to `src/` (or equivalent). A cheat that only edits tests must produce an **empty** src patch and then fail grading.

### Oracle / honest agent

Each task ships an `honest.sh` or Python honest agent that writes the correct `src/` files. Run the suite with `--agent honest` before `--agent cheat`. If honest is not 3/3, the harness or the tasks are wrong.

### Failure mode this week: applying the patch in the dirty tree

`git diff` then `pytest` in the same folder is still a trusting harness. The clean copy is the whole point. Tests will fail you if you grade in `agent_ws`.

## Must-do exercise

Folder: [exercises/week-09](../../exercises/week-09/)

Implement `capture_patch`, `replay_patch`, `grade_task`, `run_suite` in `src/mini_harness/run.py`.

```bash
uv run pytest
uv run python -m mini_harness --agent honest
uv run python -m mini_harness --agent cheat_tests
uv run python -m mini_harness --agent noop
```

Expected: honest 3/3, cheat_tests 0/3, noop 0/3.

## Stretch

- Reject patches that touch files outside `src/`.
- Record wall time per task using week 1’s `timed` idea.

## Definition of done

- [ ] Honest 3/3, cheats 0/3, noop 0/3.
- [ ] Hidden tests never appear in the agent copy.
- [ ] Grade path uses a different directory than the agent path.
- [ ] Patch is a git diff (not a tarball of the whole dirty tree).

## What breaks if you skip it

Weeks 10–12 are this design with nicer packaging. If your week 9 harness still pytest-in-place, Harbor’s separate verifier will feel like bureaucracy instead of a fix.

## Lab note

*What would make this number a lie?* Grading in the agent workspace, or capturing a diff that includes `tests/`.
