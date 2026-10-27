from __future__ import annotations

import argparse
import json
from pathlib import Path

from slice_runner.agents import honest, weak
from slice_runner.run import ROOT, run

AGENTS = {"honest": honest, "weak": weak}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent", choices=AGENTS, default="honest")
    args = parser.parse_args()
    scores = run(AGENTS[args.agent], ROOT / "artifacts" / args.agent)
    n = len(scores)
    passed = sum(scores.values())
    print(
        json.dumps(
            {
                "agent": args.agent,
                "n": n,
                "pass@1": passed / n,
                "scores": scores,
                "cost": 0,
                "mock_or_live": "mock",
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
