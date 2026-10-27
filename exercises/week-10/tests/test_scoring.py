from __future__ import annotations

import pytest

from scoring import score_reverse


@pytest.mark.parametrize(
    ("output", "target", "reward"),
    [
        ("ba", "ba", 1.0),
        ("ba\n", "ba", 1.0),
        ("The answer is ba", "ba", 0.0),
        ("ab", "ba", 0.0),
        ("", "ba", 0.0),
    ],
)
def test_score_reverse(output: str, target: str, reward: float) -> None:
    assert score_reverse(output, target) == reward
