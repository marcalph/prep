from src.two_pointers import is_palindrome
import pytest


@pytest.fixture
def palindrome_data() -> list[tuple[str, bool]]:
    inpt = ["kayak", "hello", "RCAEACAR", "a", "ABCDABCD"]
    expected = [True, False, False, True, False]
    return list(zip(inpt, expected))


def test_is_palindrome(palindrome_data: list[tuple[str, bool]]) -> None:
    for data in palindrome_data:
        inpt, expected = data
        assert is_palindrome(inpt) == expected
