import re
from aoc.utils import read_input

ms = read_input(2024, 13).split("\n")

BUTTON_PATTERN = re.compile(r"X\+(\d+), Y\+(\d+)")
PRIZE_PATTERN = re.compile(r"Prize: X=(\d+), Y=(\d+)")


def parse_input():
    _machines = []
    for i in range(0, len(ms), 4):
        btnA = tuple(int(s) for s in BUTTON_PATTERN.search(ms[i]).groups())
        btnB = tuple(int(s) for s in BUTTON_PATTERN.search(ms[i + 1]).groups())
        prize = tuple(int(s) for s in PRIZE_PATTERN.search(ms[i + 2]).groups())

        _machines.append((btnA, btnB, prize))
    return _machines


def solve(btnA, btnB, prize):
    det = btnA[0] * btnB[1] - btnA[1] * btnB[0]
    if det == 0:
        return None

    x: float = (prize[0] * btnB[1] - prize[1] * btnB[0]) / det
    if not x.is_integer():
        return None

    y: float = (-prize[0] * btnA[1] + prize[1] * btnA[0]) / det
    if not y.is_integer():
        return None

    return int(x), int(y)


def part1():
    tokens = 0
    for m in machines:
        if solution := solve(m[0], m[1], m[2]):
            tokens += 3 * int(solution[0]) + int(solution[1])

    return tokens


def part2():
    tokens = 0
    for btnA, btnB, prize in machines:
        # change prize amount
        new_prize = prize[0] + 10000000000000, prize[1] + 10000000000000
        if solution := solve(btnA, btnB, new_prize):
            tokens += 3 * int(solution[0]) + int(solution[1])

    return tokens


machines = parse_input()

ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 32067
assert ans_part_2 == 92871736253789
