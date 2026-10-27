from __future__ import annotations

import argparse
import json
from pathlib import Path

from gauntlet.loop import ROOT, changed_keys, load_config, run_config


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)
    run_p = sub.add_parser("run")
    run_p.add_argument("--config", type=Path, required=True)
    sub.add_parser("diff")
    args = parser.parse_args()
    if args.cmd == "diff":
        a = load_config(ROOT / "configs" / "baseline.json")
        b = load_config(ROOT / "configs" / "candidate.json")
        keys = changed_keys(a, b)
        print(json.dumps({"changed_keys": keys, "ok_one_lever": len(keys) == 1}, indent=2))
        return
    config = load_config(args.config)
    scores = run_config(config)
    n = len(scores)
    print(
        json.dumps(
            {
                "config": str(args.config),
                "pass@1": sum(scores.values()) / n,
                "scores": scores,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
