from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class Grade:
    reward: float
    method: str
    expected: str
    actual: str

    def to_dict(self) -> dict[str, str | float]:
        return asdict(self)


def grade_exact(output: str, expected: str, *, strip: bool = True) -> Grade:
    """
    Reward 1.0 if output equals expected, else 0.0.

    When strip=True, trim leading/trailing whitespace on both sides before
    compare. Do not collapse internal whitespace. Empty output is never a
    pass unless expected is also empty (after the same strip rule).
    """
    raise NotImplementedError
