from pathlib import Path


def test_ok() -> None:
    assert Path("out.txt").read_text(encoding="utf-8") == "ok\n"
