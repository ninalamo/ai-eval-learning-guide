from __future__ import annotations

from pathlib import Path

import pytest

from graders.score import (
    disagreement_report,
    grade_exact,
    grade_judge,
    grade_schema,
    grade_trajectory,
    load_tasks,
    score_all,
)

TASKS = load_tasks(Path(__file__).resolve().parents[1] / "data" / "tasks.json")
BY_ID = {t.id: t for t in TASKS}


def test_exact_is_case_sensitive() -> None:
    assert grade_exact(BY_ID["t1_capital"]) == 0.0
    assert grade_exact(BY_ID["t2_json"]) == 1.0
    assert grade_exact(BY_ID["t5_paraphrase"]) == 0.0


def test_schema_allows_extra_and_ignores_na() -> None:
    assert grade_schema(BY_ID["t1_capital"]) == 1.0
    assert grade_schema(BY_ID["t2_json"]) == 1.0
    assert grade_schema(BY_ID["t4_schema_wrong_city"]) == 1.0


def test_trajectory_catches_skipped_tool() -> None:
    assert grade_trajectory(BY_ID["t2_json"]) == 1.0
    assert grade_trajectory(BY_ID["t3_skipped_tool"]) == 0.0


def test_judge_accepts_paraphrase() -> None:
    assert grade_judge(BY_ID["t1_capital"]) == 1.0
    assert grade_judge(BY_ID["t5_paraphrase"]) == 1.0
    assert grade_judge(BY_ID["t4_schema_wrong_city"]) == 0.0


def test_disagreement_includes_capital_and_paraphrase() -> None:
    rows = disagreement_report(score_all(TASKS))
    ids = {r["id"] for r in rows}
    assert "t1_capital" in ids
    assert "t5_paraphrase" in ids
    assert "t3_skipped_tool" in ids


def test_judge_accuracy_is_not_one() -> None:
    scores = score_all(TASKS)
    acc = sum(s.judge == s.human_pass for s in scores) / len(scores)
    # t3: judge keywords empty → judge 1, human 0 under the spec.
    assert acc == pytest.approx(0.8)
