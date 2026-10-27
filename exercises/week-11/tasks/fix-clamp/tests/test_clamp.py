"""Hidden tests. The string hidden-canary-7f3a must not appear in instruction.md."""

import sys
from pathlib import Path

import pytest

APP = Path(__file__).resolve().parents[1]  # not used; APP_DIR is on sys.path at runtime

sys.path.insert(0, __import__("os").environ.get("APP_DIR", "/app"))

from clamp import clamp  # noqa: E402


def test_high() -> None:
    assert clamp(9, 0, 3) == 3


def test_low() -> None:
    assert clamp(-4, 0, 3) == 0


def test_inside() -> None:
    assert clamp(2, 0, 3) == 2


def test_canary_marker() -> None:
    # Marker for the instruction-leak check in verify_local.py / week lesson.
    assert "hidden-canary-7f3a"
    assert clamp(0, 0, 3) == 0
