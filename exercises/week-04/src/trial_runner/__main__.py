from __future__ import annotations

import asyncio
from pathlib import Path

from trial_runner.runner import FakeCompleter, run_trial, write_trial


async def _amain() -> None:
    workspace = Path(__file__).resolve().parents[2]
    artifacts = workspace / "artifacts"
    artifacts.mkdir(exist_ok=True)
    record = await run_trial(
        completer=FakeCompleter("4"),
        prompt="Reply with the integer 4 and nothing else.",
        expected="4",
        command=["python", "-c", "print(2+2)"],
        cwd=workspace,
    )
    out = artifacts / "demo-trial.json"
    write_trial(out, record)
    print(out)


def main() -> None:
    asyncio.run(_amain())


if __name__ == "__main__":
    main()
