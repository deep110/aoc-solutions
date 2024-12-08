from os import path
import re
from typing import Set

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

PATTERN = re.compile(r"(R|U|L|D) (\d+)")
DIRECTION = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, -1),
    "D": (0, 1),
}


def to_str(c):
    return f"{c[0]},{c[1]}"


def sign(x):
    if x == 0:
        return 0
    elif x > 0:
        return 1
    else:
        return -1


def move_tail(head_pos, tail_pos, coords: Set):
    if abs(head_pos[0] - tail_pos[0]) > 1 or abs(head_pos[1] - tail_pos[1]) > 1:
        tail_dir = (sign(head_pos[0] - tail_pos[0]), sign(head_pos[1] - tail_pos[1]))

        tail_pos[0] += tail_dir[0]
        tail_pos[1] += tail_dir[1]

        if coords:
            coords.add(to_str(tail_pos))


def part1():
    current_head = [0, 0]
    current_tail = [0, 0]
    coords = set()
    coords.add(to_str(current_tail))

    for i in ms:
        r = PATTERN.search(i)
        direction = DIRECTION[r[1]]
        length = int(r[2])

        # update head
        current_head[0] += direction[0] * length
        current_head[1] += direction[1] * length

        # update tail
        for j in range(length):
            move_tail(current_head, current_tail, coords)

    return len(coords)


def part2():
    NUM_KNOTS = 9

    current_head = [0, 0]
    tails = []
    for i in range(NUM_KNOTS):
        tails.append([0, 0])

    coords = set()
    coords.add(to_str(tails[-1]))

    for i in ms:
        r = PATTERN.search(i)
        direction = DIRECTION[r[1]]
        length = int(r[2])

        # update head
        current_head[0] += direction[0] * length
        current_head[1] += direction[1] * length

        # update tails
        for j in range(length):
            temp_head = [current_head[0], current_head[1]]
            for nt in range(NUM_KNOTS):
                if nt == 8:
                    move_tail(temp_head, tails[nt], coords)
                else:
                    move_tail(temp_head, tails[nt], None)

                temp_head[0] = tails[nt][0]
                temp_head[1] = tails[nt][1]

    return len(coords)


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 6357
assert ans_part_2 == 2627
