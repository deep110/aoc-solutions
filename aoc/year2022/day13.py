import json
import functools
from aoc.utils import read_input

ms = read_input(2022, 13).split("\n\n")


def is_right_order(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return 1
        elif left > right:
            return -1
        else:
            return 0
    elif isinstance(left, list) and isinstance(right, list):
        for i in range(len(left)):
            if i >= len(right):
                return -1

            cmp = is_right_order(left[i], right[i])

            if cmp != 0:
                return cmp

        if len(right) > len(left):
            return 1
        return 0
    else:
        if isinstance(left, int):
            return is_right_order([left], right)
        else:
            return is_right_order(left, [right])


def part1():
    pairs = []
    for i in ms:
        a, b = i.strip().split("\n")
        pairs.append((json.loads(a), json.loads(b)))

    right_order_sum = 0
    for i in range(len(pairs)):
        ro = is_right_order(pairs[i][0], pairs[i][1])
        if ro == 1:
            right_order_sum += i + 1

    return right_order_sum


def part2():
    packets = []
    for i in ms:
        a, b = i.strip().split("\n")
        packets.append(json.loads(a))
        packets.append(json.loads(b))

    # add divider packets
    packets.append([[2]])
    packets.append([[6]])

    packets.sort(key=functools.cmp_to_key(is_right_order), reverse=True)

    decoder_key = 1
    for i, p in enumerate(packets):
        if len(p) == 1 and isinstance(p[0], list) and len(p[0]) == 1:
            if p[0][0] == 6 or p[0][0] == 2:
                decoder_key *= i + 1

    return decoder_key


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 5588
assert ans_part_2 == 23958
