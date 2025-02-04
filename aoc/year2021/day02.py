"""
# Day 2: Dive!
"""

from aoc.utils import read_input

ms = [i.split(" ") for i in read_input(2021, 2).split("\n")]


def part1():
    x = 0
    y = 0
    for command in ms:
        val = int(command[1])

        if command[0] == "up":
            y -= val
        elif command[0] == "down":
            y += val
        elif command[0] == "forward":
            x += val

    return x * y


def part2():
    x = 0
    y = 0
    aim = 0
    for command in ms:
        val = int(command[1])

        if command[0] == "up":
            aim -= val
        elif command[0] == "down":
            aim += val
        elif command[0] == "forward":
            x += val
            y += aim * val

    return x * y


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution:", ans_part_1)
print("Part2 solution:", ans_part_2)

assert ans_part_1 == 1561344
assert ans_part_2 == 1848454425
