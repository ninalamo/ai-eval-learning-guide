> **Platforms:** Fedora, Ubuntu, macOS, Windows — [setup guide](../../curriculum/setup-your-machine.md). Use `uv run` from this folder after `uv sync`. On Windows, `cd exercises\week-NN` or forward slashes both work.

# Week 11 exercise — two Harbor-format tasks

Fill `instruction.md`, `tests/test.sh`, and `solution/solve.sh` for both tasks.
`verify_local.py` is provided so you do not need the Harbor CLI.

```bash
cd exercises/week-11
uv run python verify_local.py
```

Scripts should write `${LOGS_DIR:-/logs/verifier}/reward.txt`. The helper sets `APP_DIR` and `LOGS_DIR` so you can run without Docker. In Harbor, the same scripts use `/app` and `/logs/verifier`.

The string `hidden-canary-7f3a` lives in clamp’s hidden test. It must **not** appear in any instruction.
