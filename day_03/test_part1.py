import pytest

import part1
from part1 import Coord


@pytest.mark.parametrize(
    ("start", "instructions", "expected_coords"),
    [
        (Coord(0, 0), ["U3"], [Coord(0, 0), Coord(0, 1), Coord(0, 2), Coord(0, 3)],),
        (Coord(0, 0), ["D3"], [Coord(0, 0), Coord(0, -1), Coord(0, -2), Coord(0, -3)],),
        (Coord(0, 0), ["R3"], [Coord(0, 0), Coord(1, 0), Coord(2, 0), Coord(3, 0)],),
        (Coord(0, 0), ["L3"], [Coord(0, 0), Coord(-1, 0), Coord(-2, 0), Coord(-3, 0)],),
        (
            Coord(0, 0),
            ["U1", "R1", "D1", "L1"],
            [Coord(0, 0), Coord(0, 1), Coord(1, 1), Coord(1, 0), Coord(0, 0)],
        ),
    ],
)
def test_enum_wire(start, instructions, expected_coords):
    assert part1.enum_wire(instructions, start) == expected_coords


def test_find_crossings():
    start = Coord(0, 0)
    wire_a = ["R5", "U3", "L10"]
    wire_b = ["U6", "L2", "D6"]
    expected_crossings = [Coord(0, 3), Coord(-2, 3)]
    actual_crossings = part1.find_crossings(wire_a, wire_b, start)
    assert set(expected_crossings) == set(actual_crossings)


@pytest.mark.parametrize(
    ("point_a", "point_b", "expected"),
    [(Coord(0, 0), Coord(3, 5), 8), (Coord(-1, 5), Coord(2, 4), 4),],
)
def test_calc_manhattan_distance(point_a, point_b, expected):
    assert part1.calc_manhattan_distance(point_a, point_b) == expected


def test_find_nearest_crossing():
    start = Coord(0, 0)
    wire_a = ["R5", "U3", "L10"]
    wire_b = ["U6", "L2", "D6"]
    expected_crossing = Coord(0, 3)
    expected_distance = 3
    nearest_crossing = part1.find_nearest_crossing(wire_a, wire_b, start)
    assert nearest_crossing[0] == expected_crossing
    assert nearest_crossing[1] == expected_distance
