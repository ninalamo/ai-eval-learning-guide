# Week 10 — Inspect AI

**Time box:** ~8 hours (2 read, 4 build, 2 write-up)

## Goal

Author one Inspect **Task** (dataset + solver + scorer). Run it. Open the log. The log is the product; the pass rate is a summary of the log.

## Non-goal

The full inspect_evals registry, Kubernetes sandboxes, or a custom agent framework. One task, one model (or mock), one log.

## Job map

| Inspect piece | Your week 9 analog |
|---------------|-------------------|
| Sample / dataset | `suite/<task>/instruction.md` |
| Solver | the agent |
| Scorer | hidden tests / exact match |
| `inspect view` | reading `trial.json` by hand |
| Sandbox | the copytree you wrote |

## Readings

1. [Inspect — hello](https://inspect.aisi.org.uk/) — Task = dataset + solver + scorer. Read the CTF snippet; you will write something smaller.
2. [Inspect agents](https://inspect.aisi.org.uk/agents.html) — only the “agent basics” section. You are not writing a custom agent yet.
3. Optional: [inspect evals index](https://inspect.aisi.org.uk/evals/index.html.md) — see how coding evals are listed; do not run them all.

## Lesson

### Install

In the week 10 folder:

```bash
uv sync --all-groups
```

`inspect-ai` pulls a lot. That is fine. Pinning lives in `pyproject.toml`.

### A task is a function

```python
@task
def reverse_word() -> Task:
    return Task(
        dataset=[
            Sample(input="Reverse the word 'ab'. Reply with only the reversed word.", target="ba"),
        ],
        solver=generate(),
        scorer=exact(),
    )
```

`generate()` is “call the model once.” That is enough this week. Docker sandbox coding agents are stretch.

### Logs

```bash
uv run inspect eval src/reverse_task.py --model mockllm/model
uv run inspect view
```

`mockllm/model` is for pipeline debugging (you will also keep a unit test that does not need a live key). When you have Azure OpenAI:

```bash
uv run inspect eval src/reverse_task.py --model azure/<deployment>
```

Inspect’s Azure provider uses the same env vars you already know. If the provider name differs in your installed version, read `uv run inspect list models` rather than guessing.

### Failure mode this week: celebrating pass rate without opening a sample

A mock model that echoes the target will pass. That tests the scorer wiring, not the subject. Write in the lab note whether the run was mock, live, or oracle. Mixing those in one table is how eval reports get fired.

## Must-do exercise

Folder: [exercises/week-10](../../exercises/week-10/)

1. Implement `reverse_word` in `src/reverse_task.py` (stubs + tests tell you the sample).
2. `uv run pytest` (no network).
3. `uv run inspect eval src/reverse_task.py --model mockllm/model` (or the mock equivalent in your Inspect version). If mock is unavailable, skip live eval and keep pytest; note it.
4. Open one sample in `inspect view` or by reading the `.eval` log JSON. Write three sentences: input, output, score.

## Stretch

- Add `sandbox="docker"` and a `bash()` tool to make the model reverse a file on disk. Requires Docker Desktop (Windows/macOS) or Docker Engine (Linux). See [Setup your machine](../setup-your-machine.md).
- Swap `generate()` for `react()` with one tool.

## Definition of done

- [ ] pytest green without API keys.
- [ ] You can explain Task vs Sample vs scorer in one paragraph.
- [ ] You inspected **one** sample’s transcript, not just the summary pass rate.
- [ ] Lab note states mock vs live.

## What breaks if you skip it

Week 13’s public slice is Inspect or Harbor. If you have never opened a log, you will quote a number you cannot debug.

## Lab note

*What would make this number a lie?* A mock solver that returns `target`, reported as a model score, or a scorer that uses `includes()` so `ba` is found inside a 400-word apology.
