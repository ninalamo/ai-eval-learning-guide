from clamp import clamp


def test_high() -> None:
    assert clamp(9, 0, 3) == 3


def test_low() -> None:
    assert clamp(-2, 0, 3) == 0
