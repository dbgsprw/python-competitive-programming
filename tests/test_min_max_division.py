import pytest

from solutions.min_max_division import *

input_list = [
    [[3, 5, [2, 1, 5, 1, 2, 2, 2]], 6],
    [[3, 1, [1, 1, 1, 1, 1, 1, 1, 1, 1]], 3],
    [[3, 1, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]], 4],
    [[1, 0, [0]], 0],
    [[1, 5, [4]], 4]
]

@pytest.mark.timeout(1)
@pytest.mark.parametrize("test_input, expected ", input_list)
def test_solution(test_input, expected):
    result = solution(*test_input)

    assert result == expected
    assert type(result) == type(expected)

def test_binary_search():
    assert 2 == binary_search(0, 6, [1, 2, 3, 4, 5, 6], 3)
    assert 1 == binary_search(0, 7, [2, 3, 8, 9, 11, 13, 15], 5)
    assert 1 == binary_search(0, 5, [1, 2, 4, 5, 6], 3)
    assert 5 == binary_search(0, 5, [1, 2, 4, 5, 6], 100)
