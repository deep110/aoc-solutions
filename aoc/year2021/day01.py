"""
# Day 1: Sonar Sweep

For part 2 we can use a trick to simplify. If we consider the first 2 windows of 3 elements
each:

 ```none
   A1 A2 A3
     B1 B2 B3
```
then the middle 2 elements are always in common, so the subsequent window is greater only
if the last element is greater than the first. This means we can pick a sliding window of
size 4 and compare the first and last elements, without having to sum intermediate elements.
"""

from aoc.utils import read_input

ms = [int(i) for i in read_input(2021, 1).split("\n")]


def part1():
    num_inc = 0
    for i in range(1, len(ms)):
        if ms[i] > ms[i - 1]:
            num_inc += 1

    return num_inc


def part2():
    num_inc = 0
    for i in range(3, len(ms)):
        if ms[i] > ms[i - 3]:
            num_inc += 1

    return num_inc


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution:", ans_part_1)
print("Part2 solution:", ans_part_2)

assert ans_part_1 == 1564
assert ans_part_2 == 1611
