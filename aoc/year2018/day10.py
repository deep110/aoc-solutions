import re
import numpy as np
from aoc.utils import read_input

a = read_input(2018, 10).split("\n")


p = re.compile(r"position=<(.*), (.*)> velocity=<(.*), (.*)>")


def t(x):
    _m = p.search(x)
    return (int(_m.group(1)), int(_m.group(2))), (int(_m.group(3)), int(_m.group(4)))


a = list(map(lambda x: t(x), a))
points = list(map(lambda x: x[0], a))
velocities = list(map(lambda x: x[1], a))


def grid_size(coords):
    xmax = max(coords, key=lambda x: x[0])[0]
    ymax = max(coords, key=lambda x: x[1])[1]
    xmin = min(coords, key=lambda x: x[0])[0]
    ymin = min(coords, key=lambda x: x[1])[1]

    return xmax + 1, ymax + 1


def simulate(_cords, _vels, rate=1):
    new_cords = []
    for i, j in zip(_cords, _vels):
        k = (i[0] + j[0] * rate, i[1] + j[1] * rate)
        new_cords.append(k)
    return new_cords


def tx(n):
    z = []
    for q in n:
        if q == 0:
            z.append(".")
        else:
            z.append("#")
    return z


start_time = 10101
curr_cords = simulate(points, velocities, start_time)
a = np.zeros(grid_size(curr_cords), dtype=np.int64)

for i in curr_cords:
    a[i[0], i[1]] = 1
a = a.tolist()

# with open('test.txt', 'w') as f:
#     for m in a:
#         f.writelines(tx(m) + ["\n"])

# JEPPPEPG / GPEPPPEJ


def part1():
    pass


def part2():
    pass


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 0
assert ans_part_2 == 0
