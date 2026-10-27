# Week 2 — Quality bar

**Time box:** ~8 hours (2 read, 4 build, 2 write-up)

## Goal

Treat Python the way you treat C#: tests first, types at the public surface, linter in CI. Ship a tiny `grader` package with parametrized tests and a GitHub Actions workflow that runs pytest, ruff, and mypy.

## Non-goal

Coverage theater, pytest plugins zoo, or designing the week 6 grader taxonomy. One exact-match grader, done well.

## C# → Python map

| You already | This week |
|-------------|-----------|
| `[Fact]` / `[Theory]` + `[InlineData]` | `test_*` / `@pytest.mark.parametrize` |
| constructor injection / `IClassFixture<T>` | `@pytest.fixture` + `tmp_path` |
| analyzers + `dotnet format` | `ruff check` + `ruff format` |
| nullable + Roslyn | `mypy src` |
| GitHub Actions / ADO pipeline | `uv sync` + `uv run pytest` in CI |

## Readings

1. [pytest — how to parametrize](https://docs.pytest.org/en/stable/how-to/parametrize.html) — `parametrize`, ids. You already know `[Theory]`.
2. [pytest tmp_path](https://docs.pytest.org/en/stable/how-to/tmp_path.html) — this is your isolated output directory. Harnesses will use the same idea.
3. [ruff](https://docs.astral.sh/ruff/) — one tool instead of flake8+isort+format. Skim config in `pyproject.toml`, not the whole rule catalog.
4. Optional: [mypy getting started](https://mypy.readthedocs.io/en/stable/getting_started.html) — `disallow_untyped_defs` on *your* package only.

## Lesson

### pytest is xUnit with less ceremony

`assert actual == expected` is enough. pytest rewrites the assertion and prints a diff. Do not wrap tests in `TestCase` classes unless you miss MSTest.

`@pytest.mark.parametrize("output, expected, reward", [...])` is `[Theory]`. Give `ids=` so a failure reads like `test_grade_exact[trailing-newline]` instead of `test_grade_exact[2]`.

`tmp_path` is a `pathlib.Path` unique to the test. Write grader artifacts there. Never write into the source tree from a test.

### Fixtures are your composition root for tests

```python
@pytest.fixture
def workspace(tmp_path: Path) -> Path:
    (tmp_path / "out.txt").write_text("ok\n", encoding="utf-8")
    return tmp_path
```

Scope defaults to function (new instance per test). Session scope is a shared `WebApplicationFactory` analog — useful later for Docker images, dangerous if tests mutate the fixture.

### ruff and mypy are the PR bar

Eval code gets copied, forked, and run in CI on other people’s laptops. Style fights waste review. `ruff` is non-negotiable. `mypy` on `src/` catches the `None` you would have made `string?` in C#.

Do not type-ignore your way out of a public function. `grade_exact(...) -> Grade` must have a complete signature.

### Failure mode this week: tests that pin implementation

A test that asserts `len(inspect.signature(grade_exact).parameters) == 3` will break when you add `*, ignore_case: bool = False`. Grade **behavior**: given this output and this expected, the reward is 0 or 1. That is how you will test verifiers in week 9.

The other failure: a GitHub Action that `pip install pytest` onto `python:latest` with no pin. You already know why lockfiles exist. Use `uv sync --frozen` once you have a lockfile; for this week `uv sync --all-groups` is acceptable because the exercise `pyproject.toml` pins major versions.

## Must-do exercise

Folder: [exercises/week-02](../../exercises/week-02/)

1. Implement `grader.exact.grade_exact` and `Grade`.
2. `uv run pytest` green. The tests are already parametrized — read them before coding.
3. `uv run ruff check src tests` and `uv run ruff format src tests`.
4. `uv run mypy src`.
5. Copy `workflow/eval-ci.yml` to `.github/workflows/eval-ci.yml` at the **repo root** (create the folders) so a push would run this week’s checks. You do not have to push.

## Stretch

- Add `ignore_case: bool = False` without breaking existing tests.
- Add a second module `grader.schema` that validates a dict against a required key set. One parametrized test file.

## Definition of done

- [ ] pytest, ruff, mypy all clean on `exercises/week-02`.
- [ ] At least one test uses `@pytest.mark.parametrize` with `ids` (already in the starter — do not delete it).
- [ ] At least one test uses `tmp_path` to round-trip a `Grade` to JSON.
- [ ] Workflow file exists at repo root `.github/workflows/eval-ci.yml`.
- [ ] You can map every pytest feature you used to an xUnit equivalent in one sentence.

## What breaks if you skip it

Week 5’s cheat tests and week 9’s harness tests are pytest. If you skip fixtures and `tmp_path`, you will mutate shared directories and get order-dependent evals — the same class of bug as a trusting harness.

## Lab note

*What would make this number a lie?* An exact-match grader that `.strip()`s so aggressively it accepts an empty string as equal to `"\n"`, or a CI job that never runs `mypy` so `None` rewards silently become `0`.
