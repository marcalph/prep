import pytest
from src.two_pointers import is_palindrome, sum_of_three


@pytest.fixture
def palindrome_data() -> list[tuple[str, bool]]:
    inpt = ["kayak", "hello", "RCAEACAR", "a", "ABCDABCD"]
    expected = [True, False, False, True, False]
    return list(zip(inpt, expected))


def test_is_palindrome(palindrome_data: list[tuple[str, bool]]) -> None:
    for data in palindrome_data:
        inpt, expected = data
        assert is_palindrome(inpt) == expected


@pytest.fixture
def sum_of_three_data() -> list[tuple[tuple[list[int], int], bool]]:
    inpt = [
        ([1, -1, 0], -1),
        ([3, 7, 1, 2, 8, 4, 5], 10),
        ([3, 7, 1, 2, 8, 4, 5], 21),
        ([-1, 2, 1, -4, 5, -3], -8),
        ([-1, 2, 1, -4, 5, -3], 0),
    ]
    expected = [False, True, False, True, True]
    return list(zip(inpt, expected))


def test_sum_of_three(
    sum_of_three_data: list[tuple[tuple[list[int], int], bool]]
) -> None:
    for data in sum_of_three_data:
        inpt, expected = data
        assert sum_of_three(*inpt) == expected


@pytest.fixture
def remove_nth_last_node_data() -> list[tuple[tuple[list[int], int], list[int]]]:
    # todo(marcalph): generate appropriate fixture for linked-list testing
    pass
