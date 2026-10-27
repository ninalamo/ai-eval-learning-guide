> **Platforms:** Fedora, Ubuntu, macOS, Windows — [setup guide](../../curriculum/setup-your-machine.md). Use `uv run` from this folder after `uv sync`. On Windows, `cd exercises\week-NN` or forward slashes both work.

# Week 15 exercise — stub vs CLI adapter

```bash
cd exercises/week-15
uv sync --all-groups
uv run pytest
uv run python -m adapter --agent stub
uv run python -m adapter --agent cli
```

Fill `delta.md`. A canned `CliAgent` (argv `python canned.py`) counts if you say so. Cursor SDK is optional.
