from __future__ import annotations

import json
import sys
from pathlib import Path

from graders.score import disagreement_report, load_tasks, score_all


def main() -> None:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "data/tasks.json")
    scores = score_all(load_tasks(path))
    n = len(scores)
    def rate(attr: str) -> float:
        return sum(getattr(s, attr) for s in scores) / n

    payload = {
        "n": n,
        "exact_pass_rate": rate("exact"),
        "schema_pass_rate": rate("schema"),
        "trajectory_pass_rate": rate("trajectory"),
        "judge_pass_rate": rate("judge"),
        "human_pass_rate": rate("human_pass"),
        "judge_accuracy_vs_human": sum(
            1 for s in scores if s.judge == s.human_pass
        )
        / n,
        "disagreement": disagreement_report(scores),
    }
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
