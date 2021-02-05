from os import path
import numpy as np

class Rect:
    def __init__(self, desc=None, x=None, y=None, w=None, h=None):
        if desc:
            _q = desc.split(" ")
            _w = _q[2].split(",")
            _e = _q[3].split("x")
            self.id = _q[0]
            self.x = int(_w[0])
            self.y = int(_w[1].rstrip(":"))
            self.w = int(_e[0])
            self.h = int(_e[1])
        else:
            self.x = x
            self.y = y
            self.w = w
            self.h = h

    def __str__(self):
        return self.id

    def intersect(self, rect2: 'Rect') -> bool:
        if (rect2.x > self.x + self.w) or (self.x > (rect2.x + rect2.w)):
            return False

        if (rect2.y > self.y + self.h) or (self.y > (rect2.y + rect2.h)):
            return False

        return True

    def __eq__(self, other: 'Rect'):
        return self.id == other.id


with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

rects = list(map(lambda x: Rect(desc=x.rstrip("\n")), ms))


def part1():
    fab = np.zeros((1000, 1000))
    for i in rects:
        fab[i.x:i.x + i.w, i.y:i.y + i.h] += 1
    return np.sum(fab > 1)


def part2():
    for i in rects:
        k = 0
        for j in rects:
            k += 1
            if (not (i == j)) and i.intersect(j):
                break
        if k == len(rects):
            return i

print("Part1 solution: ", part1())
print("Part2 solution: ", part2())
