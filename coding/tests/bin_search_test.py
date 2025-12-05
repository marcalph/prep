import pytest

from coding.src.bin_search import binary_search, first_bad_version


@pytest.fixture
def binary_search_data() -> list[tuple[int, bool]]:
    inpt = [
        ([1, 6, 8, 10], 1),
        ([11, 22, 33, 44, 55, 66, 77], 33),
        ([-3, -1, 0, 11, 15], 0),
        ([-30, -27, -8, -6, -1], -1),
        ([0], 0),
    ]
    expected = [0, 2, 2, 4, 0]
    return list(zip(inpt, expected))


def test_bin_search(binary_search_data: list[tuple[int, bool]]) -> None:
    for data in binary_search_data:
        inpt, expected = data
        assert binary_search(*inpt) == expected


@pytest.fixture
def first_bad_version_data() -> list[tuple[int, bool]]:
    inpt = [38, 13, 29, 40, 23]
    expected = [28, 10, 10, 28, 19]
    return list(zip(inpt, expected))


def test_bin_search(first_bad_version_data: list[tuple[int, bool]]) -> None:
    for data in first_bad_version_data:
        inpt, expected = data
        assert first_bad_version(inpt, expected) == expected
