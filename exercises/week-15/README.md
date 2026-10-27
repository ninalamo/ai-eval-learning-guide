# Week 15 exercise — stub vs CLI adapter

```bash
cd exercises/week-15
uv sync --all-groups
uv run pytest
uv run python -m adapter --agent stub
uv run python -m adapter --agent cli
```

Fill `delta.md`. A canned `CliAgent` (argv `python canned.py`) counts if you say so. Cursor SDK is optional.
