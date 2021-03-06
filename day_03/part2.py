from collections import namedtuple
from copy import copy
from typing import List, Tuple

Coord = namedtuple("Coord", "x, y")


def get_wires() -> List[List[str]]:
    with open("input.txt") as file:
        text = file.read()
    wires = [line.split(",") for line in text.split("\n")]
    return wires


def enum_wire(instructions: List[str], start: Coord) -> List[Coord]:
    """
    Convert a list of wire instructions into a list of coordinates.
    """
    path = [copy(start)]
    for instr in instructions:
        direction = instr[0]
        distance = int(instr[1:])
        if direction == "U":
            for y in range(path[-1].y + 1, path[-1].y + 1 + distance):
                path.append(Coord(path[-1].x, y))
        elif direction == "D":
            for y in range(path[-1].y - 1, path[-1].y - distance - 1, -1):
                path.append(Coord(path[-1].x, y))
        elif direction == "L":
            for x in range(path[-1].x - 1, path[-1].x - distance - 1, -1):
                path.append(Coord(x, path[-1].y))
        elif direction == "R":
            for x in range(path[-1].x + 1, path[-1].x + 1 + distance):
                path.append(Coord(x, path[-1].y))
    return path


def find_crossings(
    path_a: List[Coord], path_b: List[Coord], start: Coord = Coord(0, 0)
) -> List[Coord]:
    crossings = set(path_a).intersection(set(path_b))
    crossings.remove(Coord(0, 0))
    return list(crossings)


def find_nearest_crossing(
    instr_a: List[str], instr_b: List[str], start: Coord = Coord(0, 0)
) -> Tuple[Coord, int]:
    path_a = enum_wire(instr_a, start)
    path_b = enum_wire(instr_b, start)
    crossings = find_crossings(path_a, path_b, start)
    min_distance = path_a.index(crossings[0]) + path_b.index(crossings[0])
    min_point = crossings[0]
    for crossing in crossings:
        distance = path_a.index(crossing) + path_b.index(crossing)
        if distance < min_distance:
            min_distance = distance
            min_point = crossing
    return (min_point, min_distance)


if __name__ == "__main__":
    wire_a, wire_b = get_wires()
    nearest_crossing = find_nearest_crossing(wire_a, wire_b)
    print(nearest_crossing)
