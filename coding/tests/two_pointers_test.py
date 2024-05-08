import pytest
from coding.src.ll import LinkedList
from src.two_pointers import is_palindrome, remove_nth_last_node, sum_of_three


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


def create_linked_list(data: list[int]) -> LinkedList:
    linked_list = LinkedList()
    linked_list.create_linked_list(data)
    return linked_list


@pytest.fixture
def remove_nth_last_node_data() -> list[tuple[tuple[list[int], int], list[int]]]:
    inpt = [
        ([1, 2, 3, 4, 5], 2),
        ([1, 2, 3, 4, 5], 1),
        ([1, 2, 3, 4, 5], 5),
        ([23, 28, 10, 5, 67, 39, 70, 28], 2),
        ([69, 8, 49, 106, 116, 112], 6),
    ]
    expected = [
        [1, 2, 3, 5],
        [1, 2, 3, 4],
        [2, 3, 4, 5],
        [23, 28, 10, 5, 67, 39, 28],
        [8, 49, 106, 116, 112],
    ]
    return list(zip(inpt, expected))


def test_remove_nth_last_node(
    remove_nth_last_node_data: list[tuple[tuple[list[int], int], list[int]]]
) -> None:
    for data in remove_nth_last_node_data:
        inpt, expected = data
        linked_list = create_linked_list(inpt[0])
        head = linked_list.head
        result = remove_nth_last_node(head, inpt[1])
        temp = result
        result_list = []
        while temp:
            result_list.append(temp.data)
            temp = temp.next
        assert result_list == expected
