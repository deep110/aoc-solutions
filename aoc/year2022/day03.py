from aoc.utils import read_input

ms = read_input(2022, 3).split("\n")


def priority(obj):
    if ord(obj) > 96:
        return ord(obj) - 96
    else:
        return ord(obj) - 38


def part1():
    total = 0
    for i in ms:
        num_obj = int(len(i) / 2)
        c1 = i[:num_obj]
        c2 = i[num_obj:]

        common = list(set(c1).intersection(c2))[0]
        total += priority(common)

    return total


def part2():
    total = 0
    for i in range(0, len(ms), 3):
        common = list(set(ms[i]).intersection(ms[i + 1], ms[i + 2]))[0]
        total += priority(common)

    return total


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 8252
assert ans_part_2 == 2828
