import pytest

from coding.src.fast_and_slow_pointers import is_happy_number


@pytest.fixture
def is_happy_number_data() -> list[tuple[int, bool]]:
    inpt = [2147483646, 1, 19, 8, 7]
    expected = [False, True, True, False, True]
    return list(zip(inpt, expected))


def test_is_happy_number(is_happy_number_data: list[tuple[int, bool]]) -> None:
    for data in is_happy_number_data:
        inpt, expected = data
        assert is_happy_number(inpt) == expected
