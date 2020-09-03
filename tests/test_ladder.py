import pytest

from solutions.ladder import solution

input_list = [
    [[[4, 4, 5, 5, 1], [3, 2, 4, 3, 1]], [5, 1, 8, 0, 1]],
    [[[50000], [1]], [0]],
]



@pytest.mark.timeout(2)
@pytest.mark.parametrize("test_input, expected ", input_list)
def test_solution(test_input, expected):
    result = solution(*test_input)

    assert result == expected
    assert type(result) == type(expected)
