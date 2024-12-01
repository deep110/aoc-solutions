from os import path
import re
from collections import Counter

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

PATTERN = re.compile(r"(\d+)\s*(\d+)")

LEFT = []
RIGHT = []

for nos in ms:
    res = PATTERN.search(nos)
    LEFT.append(int(res[1]))
    RIGHT.append(int(res[2]))


def part1():
    LEFT.sort()
    RIGHT.sort()

    distance = 0
    for i in range(len(LEFT)):
        distance += abs(LEFT[i] - RIGHT[i])
    return distance


def part2():
    c = Counter(RIGHT)
    similarity_score = 0
    for num in LEFT:
        similarity_score += c.get(num, 0) * num
    return similarity_score


print("Part1 solution: ", part1())
print("Part2 solution: ", part2())
