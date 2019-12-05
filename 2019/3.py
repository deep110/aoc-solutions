import numpy as np

with open("input/input_3.txt") as f:
    wires = f.readlines()

wires = list(map(lambda x: x.strip().split(","), wires))

def to_int(x):
    return int(x[1:])

def add(c1, c2):
    return c1[0]+c2[0], c1[1]+c2[1]

DD = {'L': (-1, 0), 'R': (1, 0), 'U': (0, 1), 'D': (0, -1)}

def get_new_corrs(c_old, steps, x, dic):
    _len = to_int(x)
    _dir = x[0]
    n_c = c_old
    n_steps = steps
    for _ in range(_len):
        n_c = add(n_c, DD[_dir])
        n_steps += 1
        dic[n_c] = n_steps

    return n_c, n_steps

points = []
for i, wire in enumerate(wires):
    c_old = (0, 0)
    steps = 0
    points.append({})
    for x in wire:
        c_old, steps = get_new_corrs(c_old, steps, x, points[i])


pointsA = set(points[0].keys())
pointsB = set(points[1].keys())
common = list(pointsA.intersection(pointsB))

def part1():
    def md(c):
        return abs(c[0]) + abs(c[1])
    dis = []
    for c in common:
        dis.append(md(c))

    print(min(dis))


def part2():
    steps = []
    for c in common:
        steps.append(points[0][c]+points[1][c])

    print(min(steps))

part1()
part2()