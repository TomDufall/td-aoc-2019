import pytest

import part2


@pytest.mark.parametrize(
    ("password", "valid"), [("112233", True), ("123444", False), ("111122", True),],
)
def test_is_valid_password(password, valid):
    assert part2.is_valid_password(password) == valid


def test_count_valid_passwords():
    assert part2.count_valid_passwords(111110, 111113) == 0
    assert part2.count_valid_passwords(111199, 111202) == 1
