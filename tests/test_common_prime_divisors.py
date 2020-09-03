import pytest

from solutions.common_prime_divisors import solution

input_list = [
    [[[15, 10, 3], [75, 30, 5]],    1],
    [[[15, 15, 10], [1875, 375, 90]],    2]
]

@pytest.mark.timeout(1)
@pytest.mark.parametrize("test_input, expected ", input_list)
def test_solution(test_input, expected):
    result = solution(*test_input)

    assert result == expected
    assert type(result) == type(expected)
