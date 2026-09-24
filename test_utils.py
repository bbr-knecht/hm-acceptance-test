from utils import placeholder, reverse_text


def test_placeholder() -> None:
    assert placeholder() == "placeholder"


def test_reverse_text() -> None:
    assert reverse_text("hello") == "olleh"
    assert reverse_text("") == ""
    assert reverse_text("a") == "a"
