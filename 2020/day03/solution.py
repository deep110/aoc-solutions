from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

ms = list(map(lambda x: x.strip(), ms))

MX = len(ms[0])
MY = len(ms)

def cell(x, y):
    return ms[y][x % MX]

def trees(slope):
    no_trees = 0
    a,b = 0, 0
    while b < MY:
        c = cell(a, b)

        if c == "#":
            no_trees += 1
        
        a += slope[0]
        b += slope[1]

    return no_trees

def part1():
    return trees((3, 1))

def part2():
    x = trees((1,1))
    y = trees((3,1))
    z = trees((5,1))
    w = trees((7,1))
    t = trees((1,2))

    return x*y*z*w*t

print("Part1 solution: ", part1())
print("Part2 solution: ", part2())
