from os import path
import numpy as np

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

def t(x):
    p = x.rstrip("\n").split(", ")
    return int(p[0]), int(p[1])


a = list(map(lambda x: t(x), a))

xmax = max(a, key=lambda x: x[0])[0]
ymax = max(a, key=lambda x: x[1])[1]

p = np.zeros((xmax + 1, ymax + 1), dtype=np.int)

def m_d(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])

def find_nearest_point(point, coordinates):
    d = 100000
    index = -1
    dis_at_last_rep = []
    for i, c in enumerate(coordinates):
        if point == c:
            index = -2
            break

        md = m_d(point, c)
        if md < d:
            index = i
            d = md
        elif md == d:
            dis_at_last_rep.append(d)

    if d in dis_at_last_rep:
        index = -1
    return index


def part1():
    for i, x in enumerate(p):
        for j, y in enumerate(x):
            p[i, j] = find_nearest_point((i, j), a)

    k = []
    for i in range(0, len(a)):
        # if (i in p[0, :]) or (i in p[-1, :]) or (i in p[:, 0]) or (i in p[:, -1]):
        #     pass
        # else:
        #     k.append(np.count_nonzero(p == i))
        k.append(np.count_nonzero(p == i))

    print(k)
    k = np.asarray(k)
    print(np.max(k), int(np.argmax(k)), a[int(np.argmax(k))])


def part2():
    def sum_points(point, coords):
        p = 0
        for i, c in enumerate(coords):
            p += m_d(point, c)
        return p < 10000

    for i, x in enumerate(p):
        for j, y in enumerate(x):
            p[i, j] = sum_points((i, j), a)

    return np.count_nonzero(p)


print("Part1 solution: ", part1())
print("Part2 solution: ", part2())
