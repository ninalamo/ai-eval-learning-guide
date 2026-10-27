> **Platforms:** Fedora, Ubuntu, macOS, Windows — [setup guide](../../curriculum/setup-your-machine.md). Use `uv run` from this folder after `uv sync`. On Windows, `cd exercises\week-NN` or forward slashes both work.

# Week 7 exercise — false wins at n=3

```bash
cd exercises/week-07
uv sync --all-groups
uv run pytest
uv run python -m stats_sim
```

`false_win_n3` must return a reproduced case: same true p, n=3, candidate point estimate higher, overlapping 95% bootstrap CIs.
