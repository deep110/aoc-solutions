from os import path
import numpy as np


with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()


grid_serial = 7400


def power(x, y):
    rid = x + 10
    pl = rid * y + grid_serial

    t = pl * rid
    if len(str(t)) >= 3:
        return int(str(t)[-3]) - 5
    else:
        return -5


grid = np.zeros((300, 300), dtype=np.int)

for i, _x in enumerate(grid):
    for j, _y in enumerate(_x):
        grid[i, j] = power(i + 1, j + 1)


def find_largest(size):
    te_si = 300 - size
    q = np.zeros((te_si, te_si), dtype=np.int)

    for i in range(te_si):
        for j in range(te_si):
            q[i, j] = np.sum(grid[i: i + size, j:j + size])

    z = np.argmax(q)
    p, q = z // te_si, z % te_si

    return p+1, q+1, size, np.sum(grid[p: p + size, q:q + size])


k = []
for i in range(1, 399):
    _o = find_largest(i)
    k.append(_o)

print(max(k, key=lambda x: x[3]))



def part1():
    pass

def part2():
    pass

print("Part1 solution: ", part1())
print("Part2 solution: ", part2())
