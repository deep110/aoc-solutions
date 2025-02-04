"""
# Day 7: The Treachery of Whales

For Part1, The trick is realizing that the fuel will be minium at median.

And for Part2, it will be minimum at mean. However since this could a floating point value [It is for
my input] and we are using integers we need to check 3 values total, the rounded result and one value
on either side to ensure the correct answer.
"""

from typing import List
from aoc.utils import read_input

ms = read_input(2021, 7)
positions = list(map(lambda x: int(x), ms.split(",")))


def calc_median(values: List[int]):
    values.sort()
    half_len = len(values) // 2

    if len(values) % 2 == 1:
        return values[half_len]
    else:
        return (values[half_len - 1] + values[half_len]) // 2


def part1():
    least_fuel = 0
    median_position = calc_median(positions)
    for pos in positions:
        least_fuel += abs(pos - median_position)

    return least_fuel


def part2():
    def sum_to_n(n):
        return (n * (n + 1)) // 2

    rounded_mean = sum(positions) // len(positions)

    # we calculate fuel for rounded mean and two values around it
    fuel_1 = sum(sum_to_n(abs(pos - rounded_mean)) for pos in positions)
    fuel_2 = sum(sum_to_n(abs(pos - rounded_mean - 1)) for pos in positions)
    fuel_3 = sum(sum_to_n(abs(pos - rounded_mean + 1)) for pos in positions)

    return min(fuel_1, fuel_2, fuel_3)


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution:", ans_part_1)
print("Part2 solution:", ans_part_2)

assert ans_part_1 == 344535
assert ans_part_2 == 95581659
