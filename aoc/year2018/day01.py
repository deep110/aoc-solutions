import itertools
from aoc.utils import read_input

ms = list(map(lambda x: int(x), read_input(2018, 1).split("\n")))


def part1():
    return sum(ms)


def part2():
    z = 0
    curr = {0}

    for i in itertools.cycle(ms):
        z += i

        if z in curr:
            return z
        else:
            curr.add(z)


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 416
assert ans_part_2 == 56752
