from pathlib import Path


def test_hi() -> None:
    assert Path("greet.txt").read_text(encoding="utf-8") == "hi\n"
