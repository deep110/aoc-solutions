"""
# The N-Body Problem
"""

import re
from aoc.utils import read_input

COORD_PATTERN = re.compile(r"<x=(-?\d+), y=(-?\d+), z=(-?\d+)>")

ms = read_input(2019, 12).split("\n")


class Moon:
    def __init__(self, x, y, z):
        self.position = (x, y, z)
        self.velocity = (0, 0, 0)

    def __repr__(self):
        return f"<Moon({self.position=} {self.velocity=})>"


def part1():
    moons = []
    for m in ms:
        grps = COORD_PATTERN.match(m).groups()
        moons.append(Moon(int(grps[0]), int(grps[1]), int(grps[2])))

        print(moons[-1])


def part2():
    pass


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 0
assert ans_part_2 == 0
