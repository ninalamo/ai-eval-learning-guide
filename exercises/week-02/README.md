> **Platforms:** Fedora, Ubuntu, macOS, Windows — [setup guide](../../curriculum/setup-your-machine.md). Use `uv run` from this folder after `uv sync`. On Windows, `cd exercises\week-NN` or forward slashes both work.

# Week 2 exercise — exact-match grader + quality bar

```bash
cd exercises/week-02
uv sync --all-groups
uv run pytest
uv run ruff check src tests
uv run ruff format src tests
uv run mypy src
```

Copy `workflow/eval-ci.yml` to the repo root as `.github/workflows/eval-ci.yml` when you want CI.
