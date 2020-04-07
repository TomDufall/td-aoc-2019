from collections import namedtuple
from typing import List, Tuple

Range = namedtuple("Range", "min, max")


def get_input() -> Range:
    with open("input.txt") as file:
        text = file.read()
    min_, max_ = text.split("-", 1)
    return Range(int(min_), int(max_))


def is_valid_password(password: str) -> bool:
    # Length must be 6
    if len(password) != 6:
        return False

    # Must have two adjacent matching digits, not part of a larger group
    digit_pair = False
    for i in range(len(password) - 1):
        if password[i] == password[i + 1] and password.count(password[i]) == 2:
            digit_pair = True
            break
    if not digit_pair:
        return False

    # Digits must never decrease left to right
    for i in range(1, len(password)):
        if password[i] < password[i - 1]:
            return False

    return True


def count_valid_passwords(min_: int, max_: int) -> int:
    passwords = (str(num) for num in range(min_, max_ + 1))
    return sum(1 for _ in filter(is_valid_password, passwords))


if __name__ == "__main__":
    range_ = get_input()
    print(count_valid_passwords(range_.min, range_.max))
