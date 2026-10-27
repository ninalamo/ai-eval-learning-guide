from add_one import add_one


def test_ten() -> None:
    assert add_one(10) == 11


def test_zero() -> None:
    assert add_one(0) == 1
