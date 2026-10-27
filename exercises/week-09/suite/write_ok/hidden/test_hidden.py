from pathlib import Path


def test_out_txt() -> None:
    text = Path("src/out.txt").read_text(encoding="utf-8")
    assert text == "ok\n"
