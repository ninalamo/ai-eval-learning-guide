from __future__ import annotations

from pathlib import Path


def honest(workspace: Path, task: str) -> None:
    src = workspace / "src"
    if task == "reverse":
        (src / "reverse.py").write_text(
            "def reverse(s: str) -> str:\n    return s[::-1]\n", encoding="utf-8"
        )
    elif task == "clamp":
        (src / "clamp.py").write_text(
            "def clamp(x: int, lo: int, hi: int) -> int:\n    return min(hi, max(lo, x))\n",
            encoding="utf-8",
        )
    elif task == "write_ok":
        (src / "out.txt").write_text("ok\n", encoding="utf-8")
    elif task == "is_even":
        (src / "even.py").write_text(
            "def is_even(n: int) -> bool:\n    return n % 2 == 0\n", encoding="utf-8"
        )
    elif task == "greet":
        (src / "greet.txt").write_text("hi\n", encoding="utf-8")
    else:
        raise KeyError(task)


def weak(workspace: Path, task: str) -> None:
    """Discriminative: only reverse and greet."""
    if task in {"reverse", "greet"}:
        honest(workspace, task)
