# Week 9 exercise — mini-harness (patch replay)

```bash
cd exercises/week-09
uv sync --all-groups
uv run pytest
uv run python -m mini_harness --agent honest
uv run python -m mini_harness --agent cheat_tests
uv run python -m mini_harness --agent noop
```

Agents are implemented. You implement isolation, `git diff` capture, replay, hidden grading.
