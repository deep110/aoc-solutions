"""
# Inventory Management System
"""

from collections import Counter
from aoc.utils import read_input

box_ids = read_input(2018, 2).split("\n")


def part1():
    twos = 0
    threes = 0

    for id in box_ids:
        q = Counter(id)
        vals = list(q.values())
        if 2 in vals:
            twos += 1

        if 3 in vals:
            threes += 1

    return twos * threes


def part2():
    width = len(box_ids[0])
    for i in range(width):
        seen = set()

        for id in box_ids:
            # Replace character at position i with * to create a pattern
            pattern = id[:i] + "*" + id[i + 1 :]

            # If we've seen this pattern before, we found our match
            if pattern in seen:
                return pattern.replace("*", "")

            seen.add(pattern)


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 8892
assert ans_part_2 == "zihwtxagifpbsnwleydukjmqv"
