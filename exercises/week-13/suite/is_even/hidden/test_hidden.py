from even import is_even


def test_two() -> None:
    assert is_even(2) is True


def test_three() -> None:
    assert is_even(3) is False
