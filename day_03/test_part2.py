import pytest

import part2
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
    assert part2.enum_wire(instructions, start) == expected_coords


def test_find_crossings():
    start = Coord(0, 0)
    path_a = [
        Coord(0, 0),
        Coord(0, 1),
        Coord(1, 1),
        Coord(1, 2),
        Coord(1, 3),
        Coord(0, 3),
    ]
    path_b = [Coord(0, 0), Coord(0, 1), Coord(0, 2), Coord(0, 3)]
    expected_crossings = [Coord(0, 1), Coord(0, 3)]
    actual_crossings = part2.find_crossings(path_a, path_b, start)
    assert set(expected_crossings) == set(actual_crossings)


@pytest.mark.parametrize(
    ("wire_a", "wire_b", "expected_distance"),
    [
        (["U1", "R1", "U3"], ["U3"], 2),
        (
            "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(","),
            "U62,R66,U55,R34,D71,R55,D58,R83".split(","),
            610,
        ),
        (
            "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(","),
            "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(","),
            410,
        ),
    ],
)
def test_find_nearest_crossing(wire_a, wire_b, expected_distance):
    start = Coord(0, 0)
    nearest_crossing = part2.find_nearest_crossing(wire_a, wire_b, start)
    assert nearest_crossing[1] == expected_distance
