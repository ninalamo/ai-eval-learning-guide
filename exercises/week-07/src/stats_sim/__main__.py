from __future__ import annotations

import json
from random import Random

from stats_sim.core import bootstrap_ci, false_win_n3, pass_rate, simulate


def main() -> None:
    win = false_win_n3()
    rng = Random(123)
    p = 0.5
    n = 100
    a = simulate(p, n, rng)
    b = simulate(p, n, rng)
    payload = {
        "false_win_n3": win,
        "n100_same_p": {
            "true_p": p,
            "baseline_rate": pass_rate(a),
            "candidate_rate": pass_rate(b),
            "baseline_ci": bootstrap_ci(a, rng=Random(1)),
            "candidate_ci": bootstrap_ci(b, rng=Random(2)),
        },
    }
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
