"""
# Password Philosophy
"""

import re
from aoc.utils import read_input

PATTERN = re.compile(r"([0-9]+)\-([0-9]+) ([a-z])\: (.*)")

ms = read_input(2020, 2).split("\n")


def part12():
    part1_valid_count = 0
    part2_valid_count = 0
    for i in ms:
        q = re.search(PATTERN, i)
        _min = int(q[1])
        _max = int(q[2])
        _letter = q[3]
        _password = q[4]

        count = _password.count(_letter)
        a = _password[_min - 1]
        b = _password[_max - 1]

        if _min <= count <= _max:
            part1_valid_count += 1

        if (a == _letter and b != _letter) or (b == _letter and a != _letter):
            part2_valid_count += 1

    return part1_valid_count, part2_valid_count


ans_part_1, ans_part_2 = part12()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 434
assert ans_part_2 == 509
