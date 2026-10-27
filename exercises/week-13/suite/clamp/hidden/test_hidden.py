from clamp import clamp


def test_high() -> None:
    assert clamp(8, 0, 3) == 3
