"""
# Report Repair

For part1, Instead of comparing every value, i.e O(n²) we can do in O(n), if we use a set to find
the diff
Similarly, for part2, we can reduce it from O(n³) to O(n²).
"""

from aoc.utils import read_input

ms = [int(i) for i in read_input(2020, 1).split("\n")]
ms_set = set(ms)
REQUIRED_SUM = 2020


def part1():
    for i in ms:
        diff = REQUIRED_SUM - i
        if diff in ms_set:
            return i * diff


def part2():
    for i in range(len(ms)):
        for j in range(i + 1, len(ms)):
            k = REQUIRED_SUM - ms[i] - ms[j]
            if k in ms_set:
                return ms[i] * ms[j] * k


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 956091
assert ans_part_2 == 79734368
