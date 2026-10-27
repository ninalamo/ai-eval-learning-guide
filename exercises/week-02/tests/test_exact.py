from __future__ import annotations

import json
from pathlib import Path

import pytest

from grader.exact import Grade, grade_exact


@pytest.mark.parametrize(
    ("output", "expected", "strip", "reward"),
    [
        ("4", "4", True, 1.0),
        ("4\n", "4", True, 1.0),
        ("  4  ", "4", True, 1.0),
        ("4\n", "4", False, 0.0),
        ("5", "4", True, 0.0),
        ("", "4", True, 0.0),
        ("", "", True, 1.0),
        ("hello world", "hello world", True, 1.0),
        ("hello  world", "hello world", True, 0.0),
    ],
    ids=[
        "plain",
        "trailing-newline-stripped",
        "sides-stripped",
        "newline-kept-when-strip-false",
        "wrong-answer",
        "empty-vs-gold",
        "both-empty",
        "phrase",
        "internal-whitespace-is-significant",
    ],
)
def test_grade_exact_cases(
    output: str, expected: str, strip: bool, reward: float
) -> None:
    grade = grade_exact(output, expected, strip=strip)
    assert grade.reward == reward
    assert grade.method == "exact"
    assert isinstance(grade, Grade)


def test_grade_roundtrip_json(tmp_path: Path) -> None:
    grade = grade_exact("ok\n", "ok", strip=True)
    path = tmp_path / "grade.json"
    path.write_text(json.dumps(grade.to_dict()), encoding="utf-8")
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert payload["reward"] == 1.0
    assert payload["method"] == "exact"
