> **Platforms:** Fedora, Ubuntu, macOS, Windows — [setup guide](../../curriculum/setup-your-machine.md). Use `uv run` from this folder after `uv sync`. On Windows, `cd exercises\week-NN` or forward slashes both work.

# Week 4 exercise — trial runner

Tests use `FakeCompleter` and must pass **without** an API key.

```bash
cd exercises/week-04
uv sync --all-groups
uv run pytest
```

Optional live call: copy `.env.example` to `.env`, fill Azure values, then run `uv run python -m trial_runner` (not required for definition of done).
