from os import path
import re

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

REG = re.compile(r"(\d+),(\d+) -> (\d+),(\d+)")

class Grid(object):
    def __init__(self, dim):
        self.data = []
        self.dims = dim
        for i in range(dim):
            self.data.append([0] * dim)

    def reset(self):
        self.data = []
        for i in range(self.dims):
            self.data.append([0] * self.dims)

    def add_line(self, pt1, pt2, is_dig=False):
        # vertical line (x1 == x2)
        if pt1[0] == pt2[0]:
            y_sign = 1 if pt1[1] < pt2[1] else -1
            for i in range(pt1[1], pt2[1]+y_sign, y_sign):
                self.data[i][pt1[0]] += 1
            return
        
        # horizontal line (y1 == y2)
        if pt1[1] == pt2[1]:
            x_sign = 1 if pt1[0] < pt2[0] else -1
            for i in range(pt1[0], pt2[0]+x_sign, x_sign):
                self.data[pt1[1]][i] += 1
            return
        
        # diagonal
        if is_dig:
            x_sign = 1 if pt1[0] < pt2[0] else -1
            y_sign = 1 if pt1[1] < pt2[1] else -1

            j = pt1[1]
            for i in range(pt1[0], pt2[0]+x_sign, x_sign):
                self.data[j][i] += 1
                j += y_sign
    
    def num_crossings(self):
        num_crossings = 0
        for r in self.data:
            num_crossings += sum(map(lambda x : x > 1, r))

        return num_crossings


def parse_line(line):
    g = REG.search(line)
    return ((int(g[1]), int(g[2])), (int(g[3]), int(g[4])))

# init grid
grid = Grid(1000)
coords = list(map(lambda x: parse_line(x), ms))

def part1():
    for c in coords:
        grid.add_line(c[0], c[1])

    # count no of crossings
    return grid.num_crossings()

def part2():
    grid.reset()
    for c in coords:
        grid.add_line(c[0], c[1], True)

    return grid.num_crossings()

print("Part1 solution: ", part1())
print("Part2 solution: ", part2())
