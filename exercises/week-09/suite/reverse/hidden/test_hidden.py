from reverse import reverse


def test_ab() -> None:
    assert reverse("ab") == "ba"


def test_xyz() -> None:
    assert reverse("xyz") == "zyx"
