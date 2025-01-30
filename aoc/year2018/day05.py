"""
# Alchemical Reduction

Part1, is solved using a simple stack

For Part2, one optimization is start with reacted polymer from part1, instead of fresh input.
Reduced my runtime from 120ms -> 27ms.
"""

from typing import List
from aoc.utils import read_input

ms = [ord(c) for c in list(read_input(2018, 5))]


def part1(polymer: List[int]):
    processed_polymer = []
    for p in polymer:
        if len(processed_polymer) > 0 and p ^ processed_polymer[-1] == 32:
            processed_polymer.pop()
        else:
            processed_polymer.append(p)

    return len(processed_polymer), processed_polymer


def part2(processed_polymer):
    least_len = 100000
    for i in range(ord("a"), ord("z")):
        p = filter(lambda x: x != i and x != i - 32, processed_polymer)
        processed_len, _ = part1(p)
        if processed_len < least_len:
            least_len = processed_len

    return least_len


ans_part_1, processed_polymer = part1(ms)
ans_part_2 = part2(processed_polymer)

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 9116
assert ans_part_2 == 6890
