from clamp import clamp


def test_high() -> None:
    assert clamp(9, 0, 2) == 2
