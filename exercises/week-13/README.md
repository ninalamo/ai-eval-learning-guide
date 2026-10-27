# Week 13 exercise — five-task slice + run report

```bash
cd exercises/week-13
uv sync --all-groups
uv run pytest
uv run python -m slice_runner --agent honest
uv run python -m slice_runner --agent weak
```

Fill `run-report.md`. Honest must be 5/5. Weak must not be.
