"""
# 1202 Program Alarm

Substituting symbols instead of numbers into the program shows that it calculates the value of

`a * noun + b * verb + c`

As the equation is monotonically increasing in both noun and verb, we can efficiently solve
part two by binary searching in two dimensions, instead of a slow brute force check of all
possible 10,000 combinations.
"""

from aoc.utils import read_input

TARGET = 19690720

instructions = [int(i) for i in read_input(2019, 2).split(",")]


def run_program(cs, noun, verb):
    cs[1] = noun
    cs[2] = verb
    for i in range(0, len(cs), 4):
        if cs[i] == 99:
            break
        if cs[i] == 1:
            cs[cs[i + 3]] = cs[cs[i + 1]] + cs[cs[i + 2]]
        if cs[i] == 2:
            cs[cs[i + 3]] = cs[cs[i + 1]] * cs[cs[i + 2]]

    return cs[0]


def binary_search(x1: int, x2: int, y1: int, y2: int):
    if x1 > x2 or y1 > y2:
        return None

    x = (x1 + x2) // 2
    y = (y1 + y2) // 2
    result = run_program(instructions[:], x, y)

    if result == TARGET:
        return 100 * x + y
    elif result < TARGET:
        return binary_search(x + 1, x2, y1, y2) or binary_search(x1, x2, y + 1, y2)
    else:
        return binary_search(x1, x - 1, y1, y2) or binary_search(x1, x2, y1, y - 1)


def part1():
    return run_program(instructions.copy(), 12, 2)


def part2():
    return binary_search(0, 99, 0, 99)


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 4090689
assert ans_part_2 == 7733
