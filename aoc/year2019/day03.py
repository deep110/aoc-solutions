"""
# Crossed Wires

The input follow some implicit rules that can be used to simplify our approach:
  1. Wires cross only at right angles to each other, so we only need to consider horizontal lines
   when moving vertically and vice-versa.
  2. There is only a single vertical line at a given x coordinates and vice-versa.

This makes [`BTreeMap`] a great choice to store horizontal or vertical line segments as there
are no collisions.

First we build two maps, one vertical and one horizontal, of each line segment for the first
wire. Then we trace the steps of the second wire, looking for any intersections. We calculate
both part one and part two at the same time, by also including the distance so far
from the starting point of each lines.
"""

from dataclasses import dataclass
from typing import List, Tuple
from aoc.utils import read_input

wires = list(map(lambda x: x.split(","), read_input(2019, 3).split("\n")))

DIRECTIONS = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}
ORIGIN = (0, 0)


@dataclass
class Segment:
    start: Tuple[int, int]
    end: Tuple[int, int]
    distance: int


def manhattan(p1: Tuple[int, int], p2: Tuple[int, int]) -> int:
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def is_between(a: int, b: int, c: int) -> bool:
    return min(a, b) <= c <= max(a, b)


def build_btree_map(wire: List[str]):
    wire1_vertical = {}
    wire1_horizontal = {}

    start = (0, 0)
    end = (0, 0)
    distance = 0
    for path in wire:
        (dx, dy), steps = DIRECTIONS[path[:1]], int(path[1:])
        end = start[0] + steps * dx, start[1] + steps * dy

        if dx == 0:  # vertical line
            wire1_vertical[start[0]] = Segment(start, end, distance)
        else:
            wire1_horizontal[start[1]] = Segment(start, end, distance)
        start = end
        distance += steps

    return wire1_vertical, wire1_horizontal


def check_intersection(
    line: Segment,
    candidate: Tuple[int, int],
    start: Tuple[int, int],
    current_distance: int,
):
    if candidate == ORIGIN:
        return

    if is_between(line.start[0], line.end[0], candidate[0]) and is_between(
        line.start[1], line.end[1], candidate[1]
    ):
        curr_manhattan = abs(candidate[0]) + abs(candidate[1])
        curr_delay = (
            current_distance
            + manhattan(candidate, start)
            + line.distance
            + manhattan(candidate, line.start)
        )

        return curr_manhattan, curr_delay


def part12():
    # Build two maps, one for vertical segments and one for horizontal
    #
    # Idea is to have a BTreeMap, but python only has dict, so this is just dict
    # we will sort the keys to use it when ordering is required
    wire1_vertical, wire1_horizontal = build_btree_map(wires[0])

    # Trace second wire and find intersections
    start = (0, 0)
    distance = 0
    manhattan_min = 1000000000000
    wire_delay = 1000000000000
    for path in wires[1]:
        (dx, dy), steps = DIRECTIONS[path[:1]], int(path[1:])
        end = start[0] + steps * dx, start[1] + steps * dy

        if dx == 0:  # Vertical segment
            min_y_range = min(start[1], end[1])
            max_y_range = max(start[1], end[1])
            for y, line in wire1_horizontal.items():
                if min_y_range <= y <= max_y_range:
                    candidate = (start[0], y)
                    result = check_intersection(line, candidate, start, distance)
                    if result:
                        curr_manhattan, curr_delay = result
                        manhattan_min = min(manhattan_min, curr_manhattan)
                        wire_delay = min(wire_delay, curr_delay)

        else:  # Horizontal segment
            min_x_range = min(start[0], end[0])
            max_x_range = max(start[0], end[0])
            for x, line in wire1_vertical.items():
                if min_x_range <= x <= max_x_range:
                    # if lines intersect then candidate = (x, start.y) should be on line from wire1
                    candidate = (x, start[1])
                    result = check_intersection(line, candidate, start, distance)
                    if result:
                        curr_manhattan, curr_delay = result
                        manhattan_min = min(manhattan_min, curr_manhattan)
                        wire_delay = min(wire_delay, curr_delay)

        start = end
        distance += steps

    return manhattan_min, wire_delay


ans_part_1, ans_part_2 = part12()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 529
assert ans_part_2 == 20386
