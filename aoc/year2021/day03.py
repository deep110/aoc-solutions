"""
# Day 3: Binary Diagnostic
"""

from collections import Counter
from aoc.utils import read_input

ms = read_input(2021, 3).split("\n")


def get_rating(is_co2=False):
    numbers = ms.copy()
    position = 0

    while len(numbers) > 1:
        # Count bits at current position
        count = Counter(num[position] for num in numbers)

        # Determine bit criteria
        if is_co2:
            bit = "0" if count["1"] >= count["0"] else "1"
        else:
            bit = "1" if count["1"] >= count["0"] else "0"

        # Filter numbers in place
        numbers = [num for num in numbers if num[position] == bit]
        position += 1

    return int(numbers[0], 2)


def part1():
    columns = zip(*ms)
    gamma = ""
    epsilon = ""

    for column in columns:
        if column.count("1") > column.count("0"):
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    return int(gamma, 2) * int(epsilon, 2)


def part2():
    oxygen_gen = get_rating()
    co2_scrub = get_rating(is_co2=True)

    return oxygen_gen * co2_scrub


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution:", ans_part_1)
print("Part2 solution:", ans_part_2)

assert ans_part_1 == 1071734
assert ans_part_2 == 6124992
