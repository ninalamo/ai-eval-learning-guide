# Start here

Read this once. Then open week 1. Do not re-learn software engineering.

## Your machine (all platforms)

Lessons and exercises work on **Fedora**, **Ubuntu**, **macOS**, and **Windows**. Install [uv](https://docs.astral.sh/uv/), use a project `.venv` per exercise folder, and write paths with **`pathlib`** so graders behave the same in CI and on your laptop.

Full install notes, terminals (PowerShell, Git Bash, WSL), Docker, and encoding: **[Setup your machine](setup-your-machine.md)**.

## Profile you are transferring from

Senior full-stack: C#, ASP.NET Core, Blazor, EF Core, SQL Server. Azure (OpenAI, Functions, Key Vault, App Insights). Microservices, TDD, integration tests, Docker, CI/CD. PR reviewer. Instructor of OOP and application development. Production AI feature: control-evidence health monitoring with Azure OpenAI. Daily driver: Cursor.

That is enough to *ship systems*. It is not enough to *trust an agent score*.

## The gap

| You already do | Eval engineer version |
|----------------|------------------------|
| xUnit + mocks + integration tests | Graders that the *agent cannot rewrite* |
| CI gates on green builds | Frozen suites, pass@k, CI around noisy trials |
| Azure OpenAI as a feature dependency | Models as *subjects under test* and as *judges* (two different jobs) |
| Read App Insights traces | Read agent trajectories; label a repair surface |
| PR review: “is this change correct?” | Harness review: “could a zero-capability agent still pass?” |
| Docker for deploy | Docker as the isolation boundary between agent and verifier |
| Layered / vertical-slice architecture | Task / trial / harness / grader as separate packages with contracts |

## Keep (do not study)

Git, HTTP, REST, Docker basics, CI/CD ideas, TDD *philosophy*, OOP, reading logs, writing for other engineers, Azure OpenAI as “I can call a chat model.”

## Build

1. Python as the language evals are written in (`uv`, pytest, typing, pydantic, asyncio).
2. Why a number lies: leakage, contamination, reward hacking, grader/agent shared filesystem.
3. Harbor / Inspect task format.
4. Separate-verifier grading and patch replay.
5. Statistics that survive noise.
6. A documented gauntlet loop: one lever per iteration.

## C# → Python map

Use this as a cheat sheet through weeks 1–4. After that, stop translating and think in Python.

| C# | Python |
|----|--------|
| `.csproj` + NuGet | `pyproject.toml` + `uv` |
| `dotnet restore` / `dotnet test` | `uv sync` / `uv run pytest` |
| solution folders | src layout + packages |
| `record` / DTO | `@dataclass` then **pydantic** `BaseModel` |
| `List<T>` / `Dictionary<K,V>` | `list[T]` / `dict[K, V]` |
| `T?` / `null` | `T \| None` / `None` |
| `IDisposable` / `using` | context manager / `with` |
| `Path` / `File` / `Directory` | `pathlib.Path` |
| `HttpClient` | `httpx` (sync or async) |
| `Task` / `async` | `asyncio` + `async def` |
| `Process.Start` | `subprocess.run` |
| xUnit `[Fact]` | `def test_...` |
| `[Theory]` + `[InlineData]` | `@pytest.mark.parametrize` |
| constructor injection in tests / fixtures | `@pytest.fixture` |
| `IClassFixture<T>` | module/session-scoped fixture |
| FluentAssertions / `Assert.Equal` | `assert` (pytest rewrites the assertion) |
| analyzers + `dotnet format` | `ruff` |
| nullable + Roslyn analyzers | `mypy` (or `ty`) |
| `appsettings.json` + env | `.env` + `os.environ` (never commit secrets) |
| `ILogger` | `logging` module; later: structured trial JSON |
| `JsonSerializer` | `json` stdlib; pydantic for validation |
| `Exception` / `try/catch` | `Exception` / `try/except` — catch **narrow** types |

### Idioms that will bite you

- **Indentation is the block.** There are no braces. A misplaced indent is a logic bug, not a style nit.
- **Everything is a reference**, including lists and dicts. Mutating a default argument (`def f(xs=[])`) is the classic trap. Use `None` and allocate inside.
- **No implicit interfaces.** Protocols (`typing.Protocol`) are structural, like a lightweight `interface`, but you opt in with types — the runtime will not stop a wrong object unless you check.
- **Virtual env is not optional.** `uv` creates `.venv`. Do not `pip install` into the OS Python (Linux distro packages, macOS `python3`, Windows Store Python, etc.).
- **`async` is contagious.** Mixing `httpx` async with `subprocess` sync is fine if you are explicit. Random `asyncio.run` inside already-running loops is not.
- **Packaging:** put library code under `src/<package>/`. Tests import the package, not sibling files via `sys.path` hacks.

### What “good Python” means here

Not clever. Typed public functions, pydantic at I/O boundaries, pytest for behavior, ruff for noise, one obvious way to load a JSONL trial log. That is the eval-engineer bar, not a Django tutorial.

## How a week is structured

Every [week file](weeks/) uses the same contract:

- Time box
- Goal and non-goal
- C# map (phase 1) or job map (later)
- Readings (1–3 URLs)
- Lesson (concepts + one failure mode)
- Must-do exercise
- Stretch
- Definition of done (a checklist you can fail)
- What breaks if you skip it
- Lab note: *what would make this number a lie?*

## Compression (12 weeks)

If week 1 tests are green in an evening and you are not fighting the type checker, merge weeks 1–2. If you already think in confidence intervals from A/B work, merge 7–8. If Cursor SDK is already in your muscle memory, merge 15–16. Do **not** merge 5 with 9. Isolation vs trusting the agent is the whole job.

## Tools you will actually use later

- [Inspect AI](https://inspect.aisi.org.uk/) — eval framework (dataset + solver + scorer + logs)
- [Harbor tasks](https://docs.harborframework.com/tasks/overview) — `instruction.md` + environment + verifier; format behind Terminal-Bench and SWE-bench Pro V2
- Optional: [Cursor SDK evals](https://cursor.com/docs/evals) — one real coding agent as the subject

Until week 10, you write small Python. That is deliberate. A harness you cannot explain is not a harness.
