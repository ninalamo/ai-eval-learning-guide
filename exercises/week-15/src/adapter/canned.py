"""Canned CLI stand-in: reads instruction from stdin, writes src files. Not a model."""

from __future__ import annotations

import sys
from pathlib import Path


def main() -> None:
    instruction = sys.stdin.read()
    cwd = Path.cwd()
    src = cwd / "src"
    src.mkdir(exist_ok=True)
    low = instruction.lower()
    if "reverse" in low:
        (src / "reverse.py").write_text(
            "def reverse(s: str) -> str:\n    return s[::-1]\n", encoding="utf-8"
        )
    elif "clamp" in low:
        (src / "clamp.py").write_text(
            "def clamp(x: int, lo: int, hi: int) -> int:\n    return min(hi, max(lo, x))\n",
            encoding="utf-8",
        )
    elif "out.txt" in low or "write" in low:
        (src / "out.txt").write_text("ok\n", encoding="utf-8")
    print("canned-ok")


if __name__ == "__main__":
    main()
