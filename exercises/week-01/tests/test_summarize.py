from __future__ import annotations

import json
import time
from pathlib import Path

import pytest

from summarize import (
    Summary,
    TestResult,
    load_results,
    pass_rate_by_tag,
    summarize,
    timed,
    write_summary,
)

DATA = Path(__file__).resolve().parents[1] / "data" / "results.json"


def test_load_results_uses_path_and_reads_fixture() -> None:
    rows = load_results(DATA)
    assert len(rows) == 7
    assert rows[0] == TestResult("parse_empty_input", "passed", "parser", 12)
    assert rows[-1].tag is None


def test_load_results_does_not_swallow_bad_json(tmp_path: Path) -> None:
    bad = tmp_path / "broken.json"
    bad.write_text("{not json", encoding="utf-8")
    with pytest.raises(json.JSONDecodeError):
        load_results(bad)


def test_summarize_counts_and_omits_skipped_from_tag_rates() -> None:
    summary = summarize(load_results(DATA))
    assert summary.total == 7
    assert summary.passed == 4
    assert summary.failed == 2
    assert summary.pass_rate_by_tag["parser"] == pytest.approx(0.5)
    assert summary.pass_rate_by_tag["grader"] == pytest.approx(2 / 3)
    assert "harness" not in summary.pass_rate_by_tag


def test_untagged_rows_do_not_appear_in_tag_map() -> None:
    rates = pass_rate_by_tag(load_results(DATA))
    assert None not in rates
    assert "None" not in rates


def test_pass_rate_by_tag_does_not_share_mutable_state() -> None:
    a = [
        TestResult("t1", "passed", "x", 1),
        TestResult("t2", "failed", "x", 1),
    ]
    b = [TestResult("t3", "passed", "y", 1)]
    first = pass_rate_by_tag(a)
    second = pass_rate_by_tag(b)
    assert first == {"x": 0.5}
    assert second == {"y": 1.0}
    assert "y" not in first


def test_write_summary_roundtrip(tmp_path: Path) -> None:
    out = tmp_path / "summary.json"
    original = Summary(total=2, passed=1, failed=1, pass_rate_by_tag={"g": 0.5})
    write_summary(out, original)
    payload = json.loads(out.read_text(encoding="utf-8"))
    assert payload["total"] == 2
    assert payload["pass_rate_by_tag"]["g"] == pytest.approx(0.5)


def test_timed_records_elapsed_ms() -> None:
    with timed() as t:
        time.sleep(0.02)
    assert t["elapsed_ms"] >= 15
    assert t["elapsed_ms"] < 5_000
