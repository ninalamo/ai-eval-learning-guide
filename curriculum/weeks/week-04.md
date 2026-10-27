# Week 4 — Talk to models and processes

**Time box:** ~8 hours (2 read, 4 build, 2 write-up)

## Goal

Write a trial runner that (1) gets a completion from a chat model **or** a fake, (2) optionally runs a shell command with `subprocess`, (3) persists a `trial.json` artifact, (4) exact-match scores the model text. This is the skeleton of every harness you will write.

## Non-goal

An agent loop, tool calling, Docker, or Inspect. One request, one artifact, one score. Prompt engineering as a craft is out of scope.

## C# → Python map

| You already | This week |
|-------------|-----------|
| `HttpClient` + Azure OpenAI .NET SDK | `httpx` + REST chat completions (or the official SDK if you prefer) |
| `Task` / `async` | `asyncio` + `async def` |
| `Process.Start` + timeout | `subprocess.run(..., timeout=, capture_output=True)` |
| App Insights dependency telemetry | `trial.json` you wrote on purpose |

## Readings

1. [httpx — async support](https://www.python-httpx.org/async/) — `AsyncClient`. You already know `HttpClient`; this is the Python one.
2. [subprocess](https://docs.python.org/3/library/subprocess.html) — `run`, `timeout`, `CompletedProcess`. Skim; do not use `shell=True`.
3. Azure OpenAI chat completions REST is the same shape you used in C#. If you need a refresh: [Azure OpenAI chat completions](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/how-to/chatgpt).

## Lesson

### Subject vs transport

The trial runner should depend on a **protocol**:

```python
class Completer(Protocol):
    async def complete(self, prompt: str) -> str: ...
```

`AzureOpenAICompleter` and `FakeCompleter` both satisfy it. Tests use the fake. A live key is optional this week. Eval engineers who cannot run the pipeline without a bill will skip tests, and then the pipeline rots.

### Azure env (when you go live)

Same secrets model as your day job. Local `.env` (gitignored). Variables:

- `AZURE_OPENAI_ENDPOINT`
- `AZURE_OPENAI_API_KEY`
- `AZURE_OPENAI_DEPLOYMENT`
- `AZURE_OPENAI_API_VERSION` (pin it)

Never log the key. Never put the prompt *and* the gold in the same user message if you are measuring the model — that is leakage (week 5). This week’s gold is applied **after** the completion, in the grader.

### subprocess is a sandbox you have not sandboxed yet

```python
subprocess.run(
    ["python", "-c", "print(2+2)"],
    cwd=workspace,
    capture_output=True,
    text=True,
    timeout=10,
    check=False,
)
```

`shell=True` with an interpolated instruction is how an agent instruction becomes RCE on the **harness host**. Pass argument lists. `cwd` into a scratch dir (`tmp_path` in tests). Timeouts are not optional; models hang, so do child processes.

You are **not** isolating this week. Isolation is week 9. You are learning the API so week 9 is not also “how does subprocess work.”

### Artifacts are the product

A trial file should be enough to debug a failure without re-running the model:

```json
{
  "prompt": "...",
  "completion": "...",
  "command": ["python", "-c", "print(2+2)"],
  "command_stdout": "4\n",
  "command_returncode": 0,
  "expected": "4",
  "reward": 1.0
}
```

If you only store `reward`, week 8 has nothing to classify.

### Failure mode this week: scoring in the same breath as generating

If `complete()` appends the expected answer “for convenience,” you are not evaluating the model. Keep gold on disk, load it in the grader, never in the completer. `FakeCompleter` should return a canned string set by the **test**, not by reading `expected`.

## Must-do exercise

Folder: [exercises/week-04](../../exercises/week-04/)

1. Implement `FakeCompleter`, `run_trial`, `score_exact`, `write_trial`.
2. Optional: `AzureOpenAICompleter` behind env vars. Tests must pass **without** credentials (`FakeCompleter`).
3. `uv run pytest`.
4. Produce one `artifacts/demo-trial.json` (gitignored under `artifacts/`; write it locally) using the fake.

## Stretch

- `AzureOpenAICompleter` against a cheap deployment; save the real trial next to the fake one and diff the schema (not the text).
- Add `timeout_sec` to `run_trial` and a test that a `sleep 5` command with timeout 0.2 raises or records a timeout field.

## Definition of done

- [ ] Tests green with no API key.
- [ ] `trial.json` contains prompt, completion, expected, reward — not reward alone.
- [ ] `subprocess` is invoked with a list of args, `cwd`, `timeout`, and `shell=False`.
- [ ] Completer does not receive the gold string.

## What breaks if you skip it

Week 9’s harness is this runner plus isolation. Week 15’s agent adapter is this runner plus a real CLI. If artifacts are an afterthought, failure taxonomy is fan fiction.

## Lab note

*What would make this number a lie?* A fake completer that returns `expected`, or a subprocess call with `shell=True` and the model’s raw completion interpolated into the command line.
