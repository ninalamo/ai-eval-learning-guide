# Week 15 — Real agent as subject

**Time box:** ~8 hours (2 read, 4 build, 2 write-up)

## Goal

Wrap a **real** agent (CLI or Cursor SDK) behind the same protocol as the stub. Score the working tree with your verifier. Compare stub vs real on three tasks. Explain the delta (trajectory vs outcome).

## Non-goal

Replacing your day-job IDE workflow. Training. Multi-agent orchestration.

## Job map

```python
class Agent(Protocol):
    def run(self, instruction: str, cwd: Path) -> AgentResult: ...
```

`StubAgent` is week 9 honest/noop. `CliAgent` shells out to `cmd` with the instruction on stdin or as argv. `CursorAgent` is optional (`Agent.prompt` from the Cursor SDK) if you have a key.

The harness from week 9 calls `agent.run` then patch-replays. Do not skip replay because “the CLI is trusted.”

## Readings

1. [Cursor — run Cursor in your evals](https://cursor.com/docs/evals) — `Agent.prompt` against a local cwd, then score the tree. Optional if you use a CLI instead.
2. Harbor [instruction vs prompt](https://docs.harborframework.com/tasks/instruction) — the task instruction is an input to the agent, not the agent’s system prompt.
3. Week 9 mini-harness code you wrote.

## Lesson

### Outcome vs trajectory

A real agent may pass hidden tests with a messy path (30 tool calls, a reverted file). A stub passes with one write. If you only publish outcome, you cannot see cost or reward hacking. Record `tool_call_count` when the CLI gives you logs; otherwise record wall time.

### Failure mode this week: scoring the stub and the real agent with different verifiers

Same hidden tests, same replay. If you “just pytest in the Cursor workspace” you rolled back to week 5.

### Secrets

`.env` for `CURSOR_API_KEY` or CLI tokens. Never log them. Never commit `artifacts/` with transcripts that contain keys.

## Must-do exercise

Folder: [exercises/week-15](../../exercises/week-15/)

1. Implement `StubAgent` (honest on the three tasks) and `CliAgent` (even if the CLI is `python -c` that writes a canned file — the **adapter** is the point).
2. Optional live: Cursor SDK or `claude` / `cursor` CLI if installed.
3. `uv run pytest`
4. Fill `delta.md`: stub vs real (or stub vs CliAgent canned) on reverse, clamp, write_ok.

If you have no live agent, CliAgent wrapping a small Python script still counts. Say so in `delta.md`.

## Stretch

- Trajectory assertion: `CliAgent` must not run `rm -rf`. Record argv.
- Cloud vs local runtime if you use Cursor SDK.

## Definition of done

- [ ] Protocol implemented; tests green without a paid key.
- [ ] Same three tasks, same grader, two subjects.
- [ ] `delta.md` explains at least one outcome match with a trajectory difference **or** honestly says the CLI was canned.
- [ ] Patch replay still used (test locks `graded_in_agent_tree is False` if you expose it; otherwise the suite runner from week 9 is imported).

## What breaks if you skip it

Job interviews for this role will ask how you eval a *product* agent, not a `write_text` stub. The adapter is that answer.

## Lab note

*What would make this number a lie?* Different hidden tests for the stub and the real agent, or trusting the CLI’s exit code.
