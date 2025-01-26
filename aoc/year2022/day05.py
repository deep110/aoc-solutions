import re
from aoc.utils import read_input

ms = read_input(2022, 5).split("\n")

NUM_COLUMNS = 9
NUM_ROWS = 8
SEQ_PATTERN = re.compile(r"move (\d+) from (\d+) to (\d+)")

box_grid = ms[:NUM_ROWS]
box_grid.reverse()
sequence = ms[NUM_ROWS + 2 :]


def parse_input():
    crates = [[] for i in range(NUM_COLUMNS)]

    for g in box_grid:
        for i in range(NUM_COLUMNS):
            box = g[i * 4 : i * 4 + 3].strip()
            if len(box) != 0:
                crates[i].append(box[1])

    return crates


def get_message(crates):
    message = ""
    for c in crates:
        message += c[-1]

    return message


def part1():
    crates = parse_input()

    for s in sequence:
        matched = SEQ_PATTERN.match(s)
        src = int(matched[2]) - 1
        dst = int(matched[3]) - 1

        for j in range(int(matched[1])):
            crates[dst].append(crates[src].pop())

    return get_message(crates)


def part2():
    crates = parse_input()

    for s in sequence:
        matched = SEQ_PATTERN.match(s)
        src = int(matched[2]) - 1
        dst = int(matched[3]) - 1

        num_b = len(crates[src])
        temp = crates[src][num_b - int(matched[1]) : num_b]
        crates[src] = crates[src][: num_b - int(matched[1])]

        crates[dst].extend(temp)

    return get_message(crates)


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == "QGTHFZBHV"
assert ans_part_2 == "MGDMPSZTM"
