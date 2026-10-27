from title import title_case


def test_two_words() -> None:
    assert title_case("hello world") == "Hello World"
