from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from adapter.agents import CliAgent, StubAgent
from adapter.harness import ROOT, run_task

TASKS = ["reverse", "clamp", "write_ok"]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent", choices=["stub", "cli"], default="stub")
    args = parser.parse_args()
    if args.agent == "stub":
        agent = StubAgent()
    else:
        agent = CliAgent([sys.executable, str(ROOT / "src" / "adapter" / "canned.py")])
    rows = {}
    for task in TASKS:
        result, reward = run_task(agent, task, ROOT / "artifacts" / args.agent / task)
        rows[task] = {
            "reward": reward,
            "tool_call_count": result.tool_call_count,
            "argv": result.argv,
        }
    print(json.dumps({"agent": args.agent, "rows": rows}, indent=2))


if __name__ == "__main__":
    main()
