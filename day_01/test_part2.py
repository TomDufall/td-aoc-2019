import pytest

import part2


@pytest.mark.parametrize(
    ("module_mass", "expected_fuel"), [(14, 2), (1969, 966), (100756, 50346)]
)
def test_calc_module_fuel(module_mass, expected_fuel):
    assert part2.calc_module_fuel(module_mass) == expected_fuel


def test_calc_total_fuel():
    assert part2.calc_total_fuel([14, 1969, 100756]) == 51314
