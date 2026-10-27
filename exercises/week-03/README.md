# Week 3 exercise — JSONL trials to pass@k

```bash
cd exercises/week-03
uv sync --all-groups
uv run pytest
uv run python -m metrics data/trials.jsonl
```

Row-average of `passed` on this file is **not** pass@1. Tests lock that in.
