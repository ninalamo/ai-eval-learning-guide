from __future__ import annotations

import json
import sys
from pathlib import Path

from taxonomy.check import check_answers, grade_answers, load_answers

ROOT = Path(__file__).resolve().parents[2]


def main() -> None:
    cmd = sys.argv[1] if len(sys.argv) > 1 else "check"
    answers_path = ROOT / "answers.json"
    if not answers_path.is_file():
        raise SystemExit("copy answers.template.json to answers.json first")
    rows = load_answers(answers_path)
    if cmd == "check":
        errors = check_answers(rows)
        if errors:
            print("\n".join(errors))
            raise SystemExit(1)
        print("schema ok")
        return
    if cmd == "grade":
        gold = load_answers(ROOT / "data" / "gold-answers.json")
        print(json.dumps(grade_answers(rows, gold), indent=2))
        return
    raise SystemExit("usage: python -m taxonomy [check|grade]")


if __name__ == "__main__":
    main()
