from __future__ import annotations

from pathlib import Path

import pytest
from pydantic import ValidationError

from metrics.report import load_trials, pass_at_1, pass_at_k, pass_rate_by_tag

DATA = Path(__file__).resolve().parents[1] / "data" / "trials.jsonl"


def test_fixture_has_twenty_rows() -> None:
    trials = load_trials(DATA)
    assert len(trials) == 20


def test_row_mean_is_not_pass_at_1() -> None:
    trials = load_trials(DATA)
    row_mean = sum(t.passed for t in trials) / len(trials)
    assert row_mean == pytest.approx(0.45)
    assert pass_at_1(trials) == pytest.approx(0.4)
    assert pass_at_k(trials, 2) == pytest.approx(0.6)
    assert pass_at_k(trials, 3) == pytest.approx(0.7)


def test_pass_rate_by_tag_uses_tasks() -> None:
    rates = pass_rate_by_tag(load_trials(DATA))
    assert rates["parser"] == pytest.approx(0.5)
    assert rates["grader"] == pytest.approx(1 / 3)
    assert rates["harness"] == pytest.approx(1 / 3)


def test_blank_lines_skipped(tmp_path: Path) -> None:
    path = tmp_path / "t.jsonl"
    path.write_text(
        '\n{"task_id": "a", "tag": "x", "trial_index": 0, "passed": true}\n\n',
        encoding="utf-8",
    )
    trials = load_trials(path)
    assert len(trials) == 1


def test_invalid_json_raises(tmp_path: Path) -> None:
    path = tmp_path / "t.jsonl"
    path.write_text("{nope\n", encoding="utf-8")
    with pytest.raises(Exception):
        load_trials(path)


def test_missing_passed_raises(tmp_path: Path) -> None:
    path = tmp_path / "t.jsonl"
    path.write_text(
        '{"task_id": "a", "tag": "x", "trial_index": 0}\n',
        encoding="utf-8",
    )
    with pytest.raises(ValidationError):
        load_trials(path)
