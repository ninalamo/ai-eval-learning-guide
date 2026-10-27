from __future__ import annotations

from pathlib import Path

from metrics.models import Trial


def load_trials(path: Path) -> list[Trial]:
    """
    Parse JSONL. Skip blank lines. Invalid JSON or schema must raise
    (do not convert a bad line into passed=False).
    """
    raise NotImplementedError


def pass_at_1(trials: list[Trial]) -> float:
    """Fraction of tasks whose trial_index 0 passed. Tasks, not rows."""
    raise NotImplementedError


def pass_at_k(trials: list[Trial], k: int) -> float:
    """Fraction of tasks with at least one pass among trial_index < k."""
    raise NotImplementedError


def pass_rate_by_tag(trials: list[Trial]) -> dict[str, float]:
    """pass@1 sliced by tag. Denominator is tasks in that tag."""
    raise NotImplementedError
