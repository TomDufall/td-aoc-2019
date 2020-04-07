import pytest

import part1


@pytest.mark.parametrize(
    ("password", "valid"),
    [("122345", True), ("111111", True), ("223450", False), ("123789", False),],
)
def test_is_valid_password(password, valid):
    assert part1.is_valid_password(password) == valid


def test_count_valid_passwords():
    assert part1.count_valid_passwords(111110, 111113) == 3
