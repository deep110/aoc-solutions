from collections import Counter
from aoc.utils import read_input

ms = read_input(2024, 1).split("\n")

LEFT = []
RIGHT = []

for nos in ms:
    res = nos.split("  ")
    # print(res)
    LEFT.append(int(res[0]))
    RIGHT.append(int(res[1]))


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


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 2000468
assert ans_part_2 == 18567089
