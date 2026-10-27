from vowels import count_vowels


def test_empty() -> None:
    assert count_vowels("") == 0


def test_hello() -> None:
    assert count_vowels("hello") == 2
