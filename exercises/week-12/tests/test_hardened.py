from __future__ import annotations

from pathlib import Path

import pytest

from attacks import drop_conftest, edit_tests, fetch_gold, honest
from hardened.run import run_attack

# import so students can compare: from weak.run import run_attack as weak_run


@pytest.fixture
def dest(tmp_path: Path) -> Path:
    return tmp_path / "agent"


def test_honest_hidden_pass(dest: Path) -> None:
    result = run_attack(honest, dest)
    assert result["hidden_reward"] == 1.0
    assert result["graded_in_agent_tree"] is False
    assert result["hidden_leaked_to_agent"] is False


def test_edit_tests_fails_hidden(dest: Path) -> None:
    result = run_attack(edit_tests, dest)
    assert result["hidden_reward"] == 0.0
    assert result["hidden_leaked_to_agent"] is False


def test_conftest_cannot_skip_hidden(dest: Path) -> None:
    result = run_attack(drop_conftest, dest)
    assert result["hidden_reward"] == 0.0


def test_network_denied(dest: Path) -> None:
    result = run_attack(fetch_gold, dest)
    assert result["network_allowed"] is False
    assert result["hidden_reward"] == 0.0
