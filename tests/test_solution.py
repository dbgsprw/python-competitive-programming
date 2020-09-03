import pytest

from solutions.soultion import solution

input_list = [
    #[['A', 'B'], 'R']
]

@pytest.mark.timeout(1)
@pytest.mark.parametrize("test_input, expected ", input_list)
def test_solution(test_input, expected):
    result = solution(*test_input)

    assert result == expected
    assert type(result) == type(expected)
