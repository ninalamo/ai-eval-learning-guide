> **Platforms:** Fedora, Ubuntu, macOS, Windows — [setup guide](../../curriculum/setup-your-machine.md). Use `uv run` from this folder after `uv sync`. On Windows, `cd exercises\week-NN` or forward slashes both work.

# Week 12 exercise — attack week 9, harden, threat-model

`src/weak/run.py` is a known-bad harness (grades in-place, diffs tests, copies hidden).  
`src/attacks.py` is finished. Implement `src/hardened/run.py`. Fill `threat-model.md`.

```bash
cd exercises/week-12
uv sync --all-groups
uv run pytest
```
