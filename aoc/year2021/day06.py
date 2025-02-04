"""
# Day 6: Lanternfish

The key optimization is that all fish of the same age behave the same, so we only
need to store the *total* of each fish per day, rather than each fish individually.
"""

from collections import defaultdict
from aoc.utils import read_input

ms = read_input(2021, 6)
counters = list(map(lambda x: int(x), ms.split(",")))


def simulate(fc_dict):
    zero_num = fc_dict[0]

    for c in range(8):
        fc_dict[c] = fc_dict[c + 1]

    fc_dict[6] += zero_num
    fc_dict[8] = zero_num


def part12(num_days):
    fc_dict = defaultdict(int)

    for i in counters:
        fc_dict[i] += 1

    for _ in range(num_days):
        simulate(fc_dict)

    return sum(fc_dict.values())


ans_part_1 = part12(80)
ans_part_2 = part12(256)

print("Part1 solution:", ans_part_1)
print("Part2 solution:", ans_part_2)

assert ans_part_1 == 371379
assert ans_part_2 == 1674303997472
