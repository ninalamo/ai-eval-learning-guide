from pathlib import Path


def test_src_exists() -> None:
    assert Path("src").is_dir()
