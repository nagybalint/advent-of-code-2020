import pytest
from task1 import get_number_at_turn

@pytest.mark.parametrize(
    'input_numbers,expected', [
        ([0,3,6], 436),
        ([1,3,2], 1),
        ([2,1,3], 10),
        ([1,2,3], 27),
        ([2,3,1], 78),
        ([3,2,1], 438),
        ([3,1,2], 1836)
    ]
)
def test_aoc_samlpes(input_numbers, expected):
    assert expected == get_number_at_turn(input_numbers, 2020)