import pytest

from solutions.fib_frog import solution

input_list = [
    [[[0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0]], 3],
    [[[0, 0, 0, 0]], 1],
    [[[1, 1, 1, 1]], 1],
    [[[0, 0, 0]], -1],
    [[[1, 1, 1]], 2],
    [[[]], 1],
    [[[0]], 1],
    [[[0, 0]], 1]
]

@pytest.mark.timeout(1)
@pytest.mark.parametrize("test_input, expected ", input_list)
def test_solution(test_input, expected):
    result = solution(*test_input)

    assert result == expected
    assert type(result) == type(expected)
