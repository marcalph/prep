import pytest

from ..src.stack import remove_duplicate_pairs


@pytest.fixture
def remove_duplicate_pairs_data() -> list[tuple[str, str]]:
    inpt = ["g", "ggaabcdeb", "abbddaccaaabcd", "aabbccdd", "aannkwwwkkkwna"]
    expected = ["g", "bcdeb", "abcd", "", "kwkwna"]
    return list(zip(inpt, expected))


def test_remove_duplicate_pairs(remove_duplicate_pairs_data: list[tuple[tuple[list[int], int], bool]]) -> None:
    for data in remove_duplicate_pairs_data:
        inpt, expected = data
        assert remove_duplicate_pairs(inpt) == expected
