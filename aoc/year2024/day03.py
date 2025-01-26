import re
from aoc.utils import read_input

ms = read_input(2024, 3)


def part1():
    pattern = re.compile(r"mul\((\d+),(\d+)\)")
    uncorr_ins = pattern.findall(ms)
    result = 0

    for p in uncorr_ins:
        result += int(p[0]) * int(p[1])
    return result


def part2():
    pattern = re.compile(r"mul\((\d+),(\d+)\)|(do\(\)|don't\(\))")
    uncorr_ins = pattern.findall(ms)
    result = 0

    enabled = True
    for p in uncorr_ins:
        if p[2] == "do()":
            enabled = True
        elif p[2] == "don't()":
            enabled = False
        elif enabled:
            result += int(p[0]) * int(p[1])
    return result


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 167090022
assert ans_part_2 == 89823704
