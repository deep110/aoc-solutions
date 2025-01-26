from aoc.utils import read_input

ms = [int(i) for i in read_input(2020, 1).split("\n")]
ms_set = set(ms)
REQUIRED_SUM = 2020


def part1():
    for i in ms:
        if (REQUIRED_SUM - i) in ms_set:
            return i * (REQUIRED_SUM - i)


def part2():
    for i in ms:
        for j in ms:
            k = REQUIRED_SUM - i - j
            if k in ms_set:
                return i * j * k


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 956091
assert ans_part_2 == 79734368
