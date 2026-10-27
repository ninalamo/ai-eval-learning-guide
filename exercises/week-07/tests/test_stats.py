from __future__ import annotations

from random import Random

import pytest

from stats_sim.core import (
    bootstrap_ci,
    false_win_n3,
    intervals_overlap,
    paired_delta,
    pass_rate,
    simulate,
)


def test_simulate_reproducible() -> None:
    a = simulate(0.5, 20, Random(1))
    b = simulate(0.5, 20, Random(1))
    assert a == b
    assert all(x in (0, 1) for x in a)


def test_pass_rate() -> None:
    assert pass_rate([1, 0, 1]) == pytest.approx(2 / 3)


def test_bootstrap_ci_contains_mean_on_large_n() -> None:
    xs = simulate(0.8, 200, Random(0))
    lo, hi = bootstrap_ci(xs, rng=Random(1), b=500)
    assert lo <= pass_rate(xs) <= hi
    assert hi - lo < 0.2


def test_paired_delta_is_per_task() -> None:
    assert paired_delta([1, 0, 1], [1, 1, 0]) == [0, 1, -1]


def test_paired_delta_rejects_length_mismatch() -> None:
    with pytest.raises(ValueError):
        paired_delta([1, 0], [1])


def test_false_win_n3_shape() -> None:
    result = false_win_n3()
    assert result["n"] == 3
    assert len(result["baseline"]) == 3
    assert len(result["candidate"]) == 3
    assert result["candidate_rate"] > result["baseline_rate"]
    assert result["baseline_true_p"] == result["candidate_true_p"]
    assert intervals_overlap(tuple(result["baseline_ci"]), tuple(result["candidate_ci"]))
