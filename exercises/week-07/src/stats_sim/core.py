from __future__ import annotations

from random import Random
from typing import Any


def simulate(p: float, n: int, rng: Random) -> list[int]:
    """n independent Bernoulli(p) draws as 0/1."""
    raise NotImplementedError


def pass_rate(xs: list[int]) -> float:
    raise NotImplementedError


def bootstrap_ci(
    xs: list[int],
    *,
    rng: Random,
    b: int = 1000,
    alpha: float = 0.05,
) -> tuple[float, float]:
    """
    Percentile bootstrap CI for the mean.
    Resample xs with replacement, length n, B times.
    Return (lower, upper) at alpha/2 and 1-alpha/2.
    """
    raise NotImplementedError


def paired_delta(baseline: list[int], candidate: list[int]) -> list[int]:
    """Per-task candidate[i] - baseline[i]. Length must match."""
    raise NotImplementedError


def intervals_overlap(a: tuple[float, float], b: tuple[float, float]) -> bool:
    return not (a[1] < b[0] or b[1] < a[0])


def false_win_n3(*, seed: int = 0) -> dict[str, Any]:
    """
    Find (or use a known seed derived from `seed`) a draw where:
    - baseline and candidate share the same true p (put it in the dict)
    - n == 3
    - candidate pass_rate > baseline pass_rate
    - 95% bootstrap CIs overlap

    Search seeds if seed=0 is not enough. Return a JSON-serializable dict
    including baseline, candidate, rates, cis, true_p, n, used_seed.
    """
    raise NotImplementedError
