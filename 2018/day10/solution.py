from os import path
import re
import numpy as np

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    a = f.readlines()


p = re.compile(r"position=<(.*), (.*)> velocity=<(.*), (.*)>")


def t(x):
    def san(y):
        return int(y.strip())

    _m = p.search(x)
    return (san(_m.group(1)), san(_m.group(2))), (san(_m.group(3)), san(_m.group(4)))


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
            z.append('.')
        else:
            z.append('#')
    return z


start_time = 10101
curr_cords = simulate(points, velocities, start_time)
a = np.zeros(grid_size(curr_cords), dtype=np.int)

for i in curr_cords:
    a[i[0], i[1]] = 1
a = a.tolist()

with open('test.txt', 'w') as f:
    for m in a:
        f.writelines(tx(m) + ["\n"])

# JEPPPEPG / GPEPPPEJ


def part1():
    pass

def part2():
    pass

print("Part1 solution: ", part1())
print("Part2 solution: ", part2())