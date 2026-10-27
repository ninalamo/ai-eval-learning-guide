from __future__ import annotations

from pathlib import Path

from slice_runner.agents import honest, weak
from slice_runner.run import TASKS, run


def test_honest_is_perfect(tmp_path: Path) -> None:
    scores = run(honest, tmp_path)
    assert set(scores) == set(TASKS)
    assert all(v == 1.0 for v in scores.values())


def test_weak_is_not_perfect(tmp_path: Path) -> None:
    scores = run(weak, tmp_path)
    assert scores["reverse"] == 1.0
    assert scores["greet"] == 1.0
    assert scores["clamp"] == 0.0
    assert sum(scores.values()) < 5
