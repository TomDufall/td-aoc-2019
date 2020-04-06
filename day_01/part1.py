from typing import List


def load_input() -> List[int]:
    with open("input.txt") as file:
        lines = file.readlines()
    masses = [int(line) for line in lines]
    return masses


def calc_module_fuel(module_mass: int) -> int:
    return module_mass // 3 - 2


def calc_total_fuel(modules: List[int]) -> int:
    return sum(map(calc_module_fuel, modules))


if __name__ == "__main__":
    print(calc_total_fuel(load_input()))
