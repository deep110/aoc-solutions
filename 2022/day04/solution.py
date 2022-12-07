from os import path
import re

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

PATTERN = re.compile(r"(\d+)-(\d+),(\d+)-(\d+)")

tasks = []
for i in ms:
    p = PATTERN.search(i)
    tasks.append([(int(p[1]), int(p[2])), (int(p[3]), int(p[4]))])

def part1():
    total = 0

    for e1, e2 in tasks:
        if (e2[0] >= e1[0] and e2[1] <= e1[1]) or (e1[0] >= e2[0] and e1[1] <= e2[1]):
            total += 1

    return total

def part2():
    total = 0

    for e1, e2 in tasks:
        if (e1[0] > e2[0]):
            if e1[0] >= e2[0] and e1[0] <= e2[1]:
                total += 1
        else:
            if e2[0] >= e1[0] and e2[0] <= e1[1]:
                total += 1

    return total

print("Part1 solution: ", part1())
print("Part2 solution: ", part2())
