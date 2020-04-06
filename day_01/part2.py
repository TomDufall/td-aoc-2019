from typing import List


def load_input() -> List[int]:
    with open("input.txt") as file:
        lines = file.readlines()
    masses = [int(line) for line in lines]
    return masses


def calc_module_fuel(module_mass: int) -> int:
    fuel_total = 0
    fuel_delta = module_mass // 3 - 2
    while fuel_delta > 0:
        fuel_total += fuel_delta
        fuel_delta = fuel_delta // 3 - 2
    return fuel_total


def calc_total_fuel(modules: List[int]) -> int:
    return sum(map(calc_module_fuel, modules))


if __name__ == "__main__":
    print(calc_total_fuel(load_input()))
