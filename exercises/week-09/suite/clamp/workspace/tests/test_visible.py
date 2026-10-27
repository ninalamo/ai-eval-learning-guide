from clamp import clamp


def test_inside() -> None:
    assert clamp(2, 0, 5) == 2
