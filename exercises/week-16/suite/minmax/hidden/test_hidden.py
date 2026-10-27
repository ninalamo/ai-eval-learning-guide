from minmax import minmax


def test_simple() -> None:
    assert minmax([3, 1, 2]) == (1, 3)
