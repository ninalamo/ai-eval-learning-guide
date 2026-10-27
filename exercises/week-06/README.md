> **Platforms:** Fedora, Ubuntu, macOS, Windows — [setup guide](../../curriculum/setup-your-machine.md). Use `uv run` from this folder after `uv sync`. On Windows, `cd exercises\week-NN` or forward slashes both work.

# Week 6 exercise — three graders, five tasks, disagreement

```bash
cd exercises/week-06
uv sync --all-groups
uv run pytest
uv run python -m graders data/tasks.json
```
