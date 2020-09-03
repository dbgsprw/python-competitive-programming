import pytest

from solutions.chocolate import solution

input_list = [
    [(10, 4),            5],
    [(10, 1),            10],
    [(1, 1),             1],
    [(1, 2),             1],
    [(10, 3),            10],
    [(10, 5),            2],
    [(1000000000, 1),    1000000000],
    [(1000000000, 2),    500000000]
]

@pytest.mark.timeout(1)
@pytest.mark.parametrize("test_input, expected ", input_list)
def test_solution(test_input, expected):
    result = solution(*test_input)

    assert result == expected
    assert type(result) == type(expected)
