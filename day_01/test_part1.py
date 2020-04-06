import pytest

import part1


@pytest.mark.parametrize(
    ("module_mass", "expected_fuel"), [(12, 2), (14, 2), (1969, 654), (100756, 33583)]
)
def test_calc_module_fuel(module_mass, expected_fuel):
    assert part1.calc_module_fuel(module_mass) == expected_fuel


def test_calc_total_fuel():
    assert part1.calc_total_fuel([12, 14, 1969, 100756]) == 34241
