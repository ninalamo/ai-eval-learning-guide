# Week 10 exercise — one Inspect task

```bash
cd exercises/week-10
uv sync --all-groups
uv run pytest
uv run inspect eval src/reverse_task.py --model mockllm/model
uv run inspect view
```

If `mockllm/model` is not valid in your Inspect version, `uv run inspect list models` and use the documented mock. pytest must pass **without** a live key.

`scoring.py` is the contract. `reverse_task.py` wires Inspect around it.
