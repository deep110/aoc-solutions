from collections import defaultdict
from aoc.utils import read_input

ms = read_input(2018, 3).split("\n")


class Rect:
    def __init__(self, desc=None):
        if desc:
            _q = desc.split(" ")
            _w = _q[2].split(",")
            _e = _q[3].split("x")
            self.id = _q[0][1:]
            self.x = int(_w[0])
            self.y = int(_w[1].rstrip(":"))
            self.w = int(_e[0])
            self.h = int(_e[1])

    def __repr__(self):
        return f"R<{self.x=}, {self.y=} {self.w=} {self.h=}>"

    def intersect(self, rect2: "Rect") -> bool:
        if (rect2.x > self.x + self.w) or (self.x > (rect2.x + rect2.w)):
            return False

        if (rect2.y > self.y + self.h) or (self.y > (rect2.y + rect2.h)):
            return False

        return True

    def __eq__(self, other: "Rect"):
        return self.id == other.id


rects = list(map(lambda x: Rect(desc=x), ms))


def part1():
    titles = defaultdict(int)
    for r in rects:
        for i in range(r.x, r.x + r.w):
            for j in range(r.y, r.y + r.h):
                titles[(i, j)] += 1

    return sum(1 for t in titles.values() if t > 1)


def part2():
    for i in rects:
        k = 0
        for j in rects:
            k += 1
            if (not (i == j)) and i.intersect(j):
                break
        if k == len(rects):
            return i.id


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 111326
assert ans_part_2 == "1019"
