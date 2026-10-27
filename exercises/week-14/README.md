> **Platforms:** Fedora, Ubuntu, macOS, Windows — [setup guide](../../curriculum/setup-your-machine.md). Use `uv run` from this folder after `uv sync`. On Windows, `cd exercises\week-NN` or forward slashes both work.

# Week 14 exercise — two gauntlet iterations

```bash
cd exercises/week-14
uv sync --all-groups
uv run python -m gauntlet run --config configs/baseline.json
cp configs/baseline.json configs/candidate.json
# edit ONE key in candidate.json
uv run python -m gauntlet diff
uv run python -m gauntlet run --config configs/candidate.json
```

Do not edit `suite.lock.json` or the hidden `p` comments in `src/gauntlet/agent.py`. Fill `lab-notebook.md`.
