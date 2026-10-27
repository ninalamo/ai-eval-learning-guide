# Week 1 — Python runtime and idioms

**Time box:** ~8 hours (2 read, 4 build, 2 write-up)

## Goal

Install a Python toolchain you would defend in a design review, then port a small C#-shaped utility: load test results, summarize them, write JSON. You leave the week able to run pytest via `uv` without touching system Python.

## Non-goal

CS 101. No “what is a variable,” no OOP primer, no web framework. You already taught those.

## C# → Python map

| You already | This week |
|-------------|-----------|
| `.csproj` + NuGet | `pyproject.toml` + `uv add` |
| `dotnet test` | `uv run pytest` |
| `record TestCaseResult(...)` | `@dataclass(frozen=True)` |
| `Path` / `File.ReadAllText` | `pathlib.Path` / `Path.read_text` |
| `using var reader = ...` | `with path.open() as f:` |
| `JsonSerializer.Deserialize` | `json.loads` (pydantic waits until week 3) |
| `Dictionary<string, double>` | `dict[str, float]` |

Read [start here](../00-start-here.md) if a type still feels like C#.

## Readings (pick these, not a dump)

1. [uv — working on projects](https://docs.astral.sh/uv/guides/projects/) — `uv init`, `uv add`, `uv run`, lockfile. This is your `dotnet` analog.
2. [pathlib](https://docs.python.org/3/library/pathlib.html) — skim `Path`, `read_text`, `/` for join. Ignore the os.path museum.
3. [dataclasses](https://docs.python.org/3/library/dataclasses.html) — `frozen`, `field`, type hints on the class.

Optional if `with` still feels magic: [contextlib](https://docs.python.org/3/library/contextlib.html) — `@contextmanager` only.

## Lesson

### Runtime

Python is installed on Fedora. **Do not use it for this course.** `uv` creates `.venv` in the exercise folder and pins dependencies in `pyproject.toml`. That isolation is the same reason you do not restore NuGet into `C:\Windows`.

```bash
cd exercises/week-01
uv sync
uv run pytest
```

`uv run` is `dotnet test --` for “run this command inside the project environment.”

### Types are documentation the tests can still ignore

`def load_results(path: Path) -> list[TestResult]:` does not enforce types at runtime. `mypy` in week 2 will. This week, write the annotations anyway so next week’s checker has something to chew.

`X | None` is `T?`. Use `None`, never a magic empty string, as “no tag.”

### Dataclasses vs records

```python
@dataclass(frozen=True)
class TestResult:
    name: str
    status: str  # "passed" | "failed" | "skipped"
    tag: str | None
    duration_ms: int
```

`frozen=True` is the closest default to a C# `record` with init-only properties. If you need to mutate, you probably wanted a new instance.

### pathlib

`Path("data") / "results.json"` is path combine. `.read_text(encoding="utf-8")` is explicit about encoding — do not rely on locale. Eval artifacts move between Linux CI and your laptop; encoding bugs show up as “the grader failed mysteriously.”

### Context managers

`with path.open(encoding="utf-8") as f:` disposes the handle. You will implement `timed()` in the exercise as a tiny `@contextmanager` so `with timed() as t:` records elapsed milliseconds. That pattern returns as trial timeouts in week 9.

### Failure mode this week: silent defaults

```python
def pass_rate_by_tag(results: list[TestResult], acc: dict[str, list[int]] = {}) -> dict[str, float]:
    ...
```

Mutable default arguments are shared across calls. This is the eval analog of a static `Dictionary` on a singleton you forgot about. Initialize with `None` and allocate inside the function.

The other failure: catching `Exception` around JSON parse and returning `[]`. Empty summaries look like “zero tests,” which later looks like a pass rate of 0.0 or a skipped run. Let it throw. Harnesses must fail loud when artifacts are garbage.

## Must-do exercise

Folder: [exercises/week-01](../../exercises/week-01/)

Port the C# sketch in `csharp-reference/TestResultSummary.cs` to Python.

1. `uv sync` in that folder (the starter `pyproject.toml` is already there — read it; you should be able to explain every key).
2. Implement the stubs in `src/summarize.py`.
3. `uv run pytest` — all tests green.
4. Run the module on `data/results.json` and keep the printed summary in your lab note.

Do not add pandas, pydantic, or HTTP. Stdlib + pytest only.

## Stretch

- Add `skipped` to the summary (count only; do not put skipped in pass-rate denominator).
- Write `summarize.py` so `uv run python -m summarize data/results.json` works as a CLI (`argparse` or `sys.argv`).

## Definition of done

- [ ] `uv run pytest` is green in `exercises/week-01` without `PYTHONPATH` hacks.
- [ ] You can explain what `uv sync` put in `.venv` vs what `pyproject.toml` declared.
- [ ] `load_results` uses `pathlib.Path`, not string concatenation.
- [ ] `timed()` is a context manager; tests cover it.
- [ ] You did **not** swallow parse errors.

## What breaks if you skip it

Every later exercise assumes `uv run pytest`. Week 3 JSONL and week 9 harnesses are pathlib-heavy. If you still think in `string path = dir + "\\" + file`, you will write graders that only work on one OS.

## Lab note

*What would make this number a lie?* For this week: a pass rate computed with skipped tests in the denominator, or a shared mutable dict across two `summarize()` calls.
