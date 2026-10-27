from __future__ import annotations

import json
import sys
from pathlib import Path

from metrics.report import load_trials, pass_at_1, pass_at_k, pass_rate_by_tag


def main() -> None:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "data/trials.jsonl")
    trials = load_trials(path)
    n_rows = len(trials)
    row_mean = sum(t.passed for t in trials) / n_rows if n_rows else 0.0
    payload = {
        "n_rows": n_rows,
        "row_mean_passed": row_mean,
        "pass@1": pass_at_1(trials),
        "pass@2": pass_at_k(trials, 2),
        "pass@3": pass_at_k(trials, 3),
        "pass@1_by_tag": pass_rate_by_tag(trials),
    }
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
