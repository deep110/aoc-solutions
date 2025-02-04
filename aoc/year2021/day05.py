"""
# Day 5: Hydrothermal Venture
"""

from collections import defaultdict
import re
from typing import Dict
from aoc.utils import read_input

ms = read_input(2021, 5).split("\n")

PATTERN = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")
WIDTH = 1000


def add_parallel_line(grid, x1, y1, x2, y2):
    # vertical line (x1 == x2)
    if x1 == x2:
        y_sign = 1 if y1 < y2 else -1
        for i in range(y1, y2 + y_sign, y_sign):
            grid[WIDTH * i + x1] += 1
        return

    # horizontal line (y1 == y2)
    if y1 == y2:
        x_sign = 1 if x1 < x2 else -1
        for i in range(x1, x2 + x_sign, x_sign):
            grid[WIDTH * y1 + i] += 1
        return


def add_diagonal_line(grid, x1, y1, x2, y2):
    x_sign = 1 if x1 < x2 else -1
    y_sign = 1 if y1 < y2 else -1

    j = y1
    for i in range(x1, x2 + x_sign, x_sign):
        grid[WIDTH * j + i] += 1
        j += y_sign


def num_crossings(grid: Dict[int, int]):
    num_crossings = 0
    for v in grid.values():
        if v > 1:
            num_crossings += 1

    return num_crossings


def parse_line(line):
    g = PATTERN.match(line)
    return (int(g[1]), int(g[2]), int(g[3]), int(g[4]))


def part12():
    coords = list(map(lambda x: parse_line(x), ms))
    grid = defaultdict(int)

    for x1, y1, x2, y2 in coords:
        add_parallel_line(grid, x1, y1, x2, y2)
    p_num_crossings = num_crossings(grid)

    for x1, y1, x2, y2 in coords:
        if x1 != x2 and y1 != y2:
            add_diagonal_line(grid, x1, y1, x2, y2)
    d_num_crossings = num_crossings(grid)

    return p_num_crossings, d_num_crossings


ans_part_1, ans_part_2 = part12()

print("Part1 solution:", ans_part_1)
print("Part2 solution:", ans_part_2)

assert ans_part_1 == 6548
assert ans_part_2 == 19663
