from __future__ import annotations

from pathlib import Path

from mini_harness.agents import cheat_tests, honest, noop
from mini_harness.run import prepare_agent_workspace, run_suite

ROOT = Path(__file__).resolve().parents[1]
SUITE = ROOT / "suite"


def test_hidden_not_copied_into_agent_ws(tmp_path: Path) -> None:
    dest = prepare_agent_workspace(SUITE / "reverse" / "workspace", tmp_path / "ws")
    names = {p.name for p in dest.rglob("*")}
    assert "test_hidden.py" not in names
    assert (dest / "src" / "reverse.py").is_file()


def test_honest_three_of_three(tmp_path: Path) -> None:
    scores = run_suite(SUITE, honest, tmp_path / "honest")
    assert scores == {"clamp": 1.0, "reverse": 1.0, "write_ok": 1.0}


def test_noop_zero(tmp_path: Path) -> None:
    scores = run_suite(SUITE, noop, tmp_path / "noop")
    assert scores == {"clamp": 0.0, "reverse": 0.0, "write_ok": 0.0}


def test_cheat_tests_zero(tmp_path: Path) -> None:
    scores = run_suite(SUITE, cheat_tests, tmp_path / "cheat")
    assert scores == {"clamp": 0.0, "reverse": 0.0, "write_ok": 0.0}
