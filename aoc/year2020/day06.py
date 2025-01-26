from aoc.utils import read_input

ms = read_input(2020, 6)
ms = ms.split("\n\n")


def part1():
    c = 0
    for i in ms:
        j = set(i.replace("\n", ""))
        c += len(j)

    return c


def part2():
    c = 0
    for i in ms:
        j = list(map(lambda x: set(x), i.strip().split("\n")))
        k = set.intersection(*j)
        c += len(k)

    return c


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 6437
assert ans_part_2 == 3229
