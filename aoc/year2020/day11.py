"""
# Seating System

Cellular automata are hard to speed up due to the need to check all neighbors each iteration.
For both parts we minimize expensive memory allocation by creating only two temporary buffers
then swapping between them each turn, a similar approach to double buffering.
"""

from collections import defaultdict
from aoc.utils import read_input

ms = read_input(2020, 11).split("\n")


DIRECTIONS = (
    (-1, 1),
    (-1, 0),
    (-1, -1),
    (0, 1),
    (0, -1),
    (1, 1),
    (1, 0),
    (1, -1),
)
SEAT_EMPTY = "L"
SEAT_OCCUPIED = "#"


def run_simulation(seats, neighbors, num_occupancy=4):
    num_rows = len(seats)
    num_columns = len(seats[0])

    # create copy of grid
    state = []
    for _ in range(num_rows):
        state.append(["."] * num_columns)

    while True:
        state_changed = False
        for i in range(num_rows):
            for j in range(num_columns):
                if seats[i][j] == ".":
                    continue

                state[i][j] = seats[i][j]
                if seats[i][j] == SEAT_EMPTY:
                    all_empty = True
                    for ni, nj in neighbors[(i, j)]:
                        if seats[ni][nj] == SEAT_OCCUPIED:
                            all_empty = False
                            break
                    if all_empty:
                        state[i][j] = SEAT_OCCUPIED

                else:
                    num_occupied = 0
                    for ni, nj in neighbors[(i, j)]:
                        if seats[ni][nj] == SEAT_OCCUPIED:
                            num_occupied += 1
                            if num_occupied >= num_occupancy:
                                state[i][j] = SEAT_EMPTY
                                break

                state_changed = state_changed or state[i][j] != seats[i][j]

        if not state_changed:
            return

        # swap seats and state grid buffer
        seats, state = state, seats


def part1():
    seats = list(map(lambda x: list(x), ms))
    NUM_ROWS = len(seats)
    NUM_COLUMNS = len(seats[0])

    # cache the neighbors which are not floors
    neighbors = defaultdict(list)
    for i in range(NUM_ROWS):
        for j in range(NUM_COLUMNS):
            for di, dj in DIRECTIONS:
                ni, nj = i + di, j + dj
                if (
                    ni < 0
                    or ni >= NUM_ROWS
                    or nj < 0
                    or nj >= NUM_COLUMNS
                    or seats[ni][nj] == "."
                ):
                    continue

                neighbors[(i, j)].append((ni, nj))

    run_simulation(seats, neighbors, 4)

    # count occupied seats
    num_occupied = 0
    for i in range(NUM_ROWS):
        for j in range(NUM_COLUMNS):
            if seats[i][j] == SEAT_OCCUPIED:
                num_occupied += 1

    return num_occupied


def part2():
    seats = list(map(lambda x: list(x), ms))
    NUM_ROWS = len(seats)
    NUM_COLUMNS = len(seats[0])

    # cache the neighbors which are not floors
    neighbors = defaultdict(list)
    for i in range(NUM_ROWS):
        for j in range(NUM_COLUMNS):
            for di, dj in DIRECTIONS:
                idx = 1
                while True:
                    ni, nj = i + idx * di, j + idx * dj
                    if ni < 0 or ni >= NUM_ROWS or nj < 0 or nj >= NUM_COLUMNS:
                        break

                    if seats[ni][nj] != ".":
                        neighbors[(i, j)].append((ni, nj))
                        break

                    idx += 1

    run_simulation(seats, neighbors, 5)

    # count occupied seats
    num_occupied = 0
    for i in range(NUM_ROWS):
        for j in range(NUM_COLUMNS):
            if seats[i][j] == SEAT_OCCUPIED:
                num_occupied += 1

    return num_occupied


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 2354
assert ans_part_2 == 2072
