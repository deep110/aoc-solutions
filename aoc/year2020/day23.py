"""
# Crab Cups

The cups form a circular [singly linked list](https://en.wikipedia.org/wiki/Linked_list).

For performance instead of using class references, we store the cups in a list where an element
at index `i` stores the index of the next cup.
For example `cup[1]` points to the first cup after cup one and `cup[cup[1]]` points to second
cup after cup one.
"""

from typing import List


input_str = "716892543"
input = [int(i) for i in list(input_str)]


def play(cups: List[int], start_cup, max_cup: int, num_rounds: int):
    current = start_cup

    p1 = p2 = p3 = -1
    for _ in range(num_rounds):
        # Step1: Skip three cups, and connect current to 4th one
        p1 = cups[current]
        p2 = cups[p1]
        p3 = cups[p2]
        cups[current] = cups[p3]

        # Step2: We need destination cup, whose label is curr value -1 or max if goes below min
        dest = current - 1 or max_cup
        while dest == p1 or dest == p2 or dest == p3:
            dest = dest - 1 or max_cup

        # Step3: Insert pickup after destination, and update current
        cups[p3] = cups[dest]
        cups[dest] = p1
        current = cups[current]

    return cups


def part1():
    num_cups = len(input)
    # Map each cup value to the next cup value
    cups = [0] * (num_cups + 1)
    for i in range(num_cups):
        cups[input[i]] = input[(i + 1) % num_cups]

    play(cups, input[0], num_cups, 100)

    value = ""
    start = 1
    for _ in range(num_cups - 1):
        start = cups[start]
        value += str(start)
    return value


def part2():
    num_cups = 1_000_000
    # Map each cup value to the next cup value
    cups = [0] * (num_cups + 1)  # +1 since we're using 1-based indexing
    for i in range(8):
        cups[input[i]] = input[i + 1]

    cups[input[8]] = 10
    for i in range(10, num_cups):
        cups[i] = i + 1
    cups[num_cups] = input[0]

    play(cups, input[0], num_cups, 10000000)

    c1 = cups[1]
    return c1 * cups[c1]


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == "49725386"
assert ans_part_2 == 538935646702
