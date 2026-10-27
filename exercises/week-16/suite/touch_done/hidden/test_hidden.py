from pathlib import Path


def test_done_exists() -> None:
    p = Path("DONE")
    assert p.is_file()
    assert p.stat().st_size == 0
