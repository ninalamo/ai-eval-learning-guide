# Week 11 — Harbor task format

**Time box:** ~8 hours (2 read, 4 build, 2 write-up)

## Goal

Author **two** Harbor-format tasks: one terminal outcome, one unit-test outcome. Instruction must not leak hidden tests. Oracle (`solution/solve.sh`) must pass your local verifier.

## Non-goal

Running Terminal-Bench at scale, Modal/Daytona, or publishing to a registry. Format literacy first.

## Job map

Harbor task directory:

```text
my-task/
  instruction.md      # agent-visible
  task.toml           # timeouts, metadata
  environment/        # Dockerfile or image
  tests/test.sh       # writes /logs/verifier/reward.txt
  solution/solve.sh   # oracle
```

You already built this split in weeks 5 and 9. Harbor is the community contract around it.

## Readings

1. [Harbor tasks overview](https://docs.harborframework.com/tasks/overview)
2. [Harbor instruction](https://docs.harborframework.com/tasks/instruction) — outcomes and absolute paths; canary comments; do not turn the instruction into the agent’s system prompt.
3. [Harbor verifier](https://docs.harborframework.com/tasks/verifier) — `reward.txt` / `reward.json`; prefer a **separate** verifier environment.

## Lesson

### Instruction vs tests

Instruction: “Write the string `hello` to `/app/out.txt`.”  
Tests: `grep -qx hello /app/out.txt`.  
If the instruction includes the grep, you leaked.

### Oracle is a harness test

`solve.sh` runs as if it were a perfect agent. If oracle fails, you do not have a task. The local helper `verify_local.py` runs solve then test in a temp dir with a fake `/logs/verifier`. You can finish this week without installing the Harbor CLI.

### Two shapes

1. **Terminal:** file or command output exists. `test.sh` is shell.
2. **Unit-test:** agent edits Python; `test.sh` runs pytest on files the agent should not have seen. Copy tests in only at verify time (the helper does this).

### Failure mode this week: teaching the instruction to pass the tests

“Do not modify tests/” in the instruction is not a security boundary. The verifier must not trust the agent’s tree. Harbor’s `environment_mode = separate` exists because people forgot this. Your local helper overlays only `solution` outputs, then copies `tests/` in.

## Must-do exercise

Folder: [exercises/week-11](../../exercises/week-11/)

Complete:

- `tasks/write-hello/` (terminal)
- `tasks/fix-clamp/` (unit-test)

`uv run python verify_local.py` must print `write-hello oracle=1` and `fix-clamp oracle=1`.

Write `instruction.md` so that a grep of it does **not** contain the hidden expected values used only in tests (`hidden-canary-7f3a` is in the clamp hidden test on purpose — it must not appear in the instruction).

## Stretch

- Install Harbor and run `harbor run` on one task with the oracle solver.
- Add a canary HTML comment at the top of each instruction.

## Definition of done

- [ ] Both oracles reward 1 via `verify_local.py`.
- [ ] `hidden-canary-7f3a` does not appear in any `instruction.md`.
- [ ] `task.toml` exists and names the task.
- [ ] You can explain why `tests/` is not in the agent-visible environment copy.

## What breaks if you skip it

SWE-bench Pro V2 and Terminal-Bench 2 ship as Harbor tasks. If you cannot author one, you cannot review one.

## Lab note

*What would make this number a lie?* An instruction that quotes the hidden canary, or a `test.sh` that `echo 1` without checking anything.
