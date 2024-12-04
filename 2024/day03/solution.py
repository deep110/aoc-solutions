from os import path
import re

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.read()


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


print("Part1 solution: ", part1())
print("Part2 solution: ", part2())
