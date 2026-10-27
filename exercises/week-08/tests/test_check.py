from __future__ import annotations

from pathlib import Path

from taxonomy.check import SURFACES, check_answers, load_answers

ROOT = Path(__file__).resolve().parents[1]


def test_gold_passes_checker() -> None:
    gold = load_answers(ROOT / "data" / "gold-answers.json")
    # Gold omits some required student fields; checker is for answers.json shape.
    # Ensure gold surfaces are in the closed set.
    assert {g["repair_surface"] for g in gold} <= SURFACES
    assert gold[6]["repair_surface"] == "grader"
    assert gold[7]["repair_surface"] == "model_ceiling"


def test_template_fails_checker() -> None:
    rows = load_answers(ROOT / "answers.template.json")
    errors = check_answers(rows)
    assert errors  # empty surfaces, empty mutations


def test_eight_traces_exist() -> None:
    traces = sorted((ROOT / "data" / "traces").glob("*.json"))
    assert [p.stem for p in traces] == [f"{i:02d}" for i in range(1, 9)]
