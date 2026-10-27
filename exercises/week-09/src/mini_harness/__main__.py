from __future__ import annotations

import argparse
import json
from pathlib import Path

from mini_harness.agents import cheat_tests, honest, noop
from mini_harness.run import run_suite

AGENTS = {"honest": honest, "cheat_tests": cheat_tests, "noop": noop}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent", choices=AGENTS, default="honest")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    scores = run_suite(
        suite_root=root / "suite",
        agent=AGENTS[args.agent],
        work_root=root / "artifacts" / args.agent,
    )
    print(json.dumps({"agent": args.agent, "scores": scores}, indent=2))


if __name__ == "__main__":
    main()
