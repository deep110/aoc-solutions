"""
# Toboggan Trajectory
"""

from aoc.utils import read_input

ms = read_input(2020, 3).split("\n")
MX = len(ms[0])
MY = len(ms)


def trees(sx, sy):
    no_trees = 0
    a, b = 0, 0
    while b < MY:
        c = ms[b][a % MX]

        if c == "#":
            no_trees += 1

        a += sx
        b += sy

    return no_trees


def part1():
    return trees(3, 1)


def part2():
    x = trees(1, 1)
    y = trees(3, 1)
    z = trees(5, 1)
    w = trees(7, 1)
    t = trees(1, 2)

    return x * y * z * w * t


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 225
assert ans_part_2 == 1115775000
