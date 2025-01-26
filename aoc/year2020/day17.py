"""
# Conway Cubes

While a solution for both parts using a state and grid and just lists was easy enough to add,
it took 1.7s to complete both parts.

Then I saw few [solutions on reddit](https://www.reddit.com/r/adventofcode/comments/keqsfa/2020_day_17_solutions/),
lot of people using python recommend using dict and key being tuple of indexes.

In my own input, only about 4% of the 3D space ended up being active, and 2% of my 4D space ends
up being active. This means that holding a dense vector of all possible active points
(which will be (6+8+6)^n) is up to 98% wasteful. Hence dict is very memory efficient, if you only
need to keep track of active coordinates.

Also, we are doing reverse, instead of looping on each coordinate and finding active neighbors, we are
looking into each active coordinate and adding 1 to each neighbor.
This also helps to speed up a lot, because state change requires some minimum active neighbors
to be present, so we only loop on coordinates which has at least 1 active neighbor.
"""

from collections import defaultdict
from itertools import product
from aoc.utils import read_input

NUM_CYCLES = 6
ms = read_input(2020, 17).split("\n")


def get_neighbors(dimension: int):
    offsets = [-1, 0, 1]
    neighbors = list(product(offsets, repeat=dimension))
    neighbors.remove((0,) * dimension)
    return neighbors


def part1():
    active_cells = set()
    neighbors = get_neighbors(3)
    y = 0
    z = 0

    for line in ms:
        for x, c in enumerate(line):
            if c == "#":
                active_cells.add((x, y, z))
        y += 1

    for _ in range(NUM_CYCLES):
        neighbor_count = defaultdict(int)
        new_active_cells = set()

        # Find each active coordinate, and for each of its neighbor add 1
        #
        # We are doing reverse, instead of looping on each coordinate and finding
        # active neighbors, we are looking into each active coordinate and adding
        # 1 to each neighbor.
        for cell in active_cells:
            for ni, nj, nk in neighbors:
                neighbor_count[(cell[0] + ni, cell[1] + nj, cell[2] + nk)] += 1

        for coord, count in neighbor_count.items():
            # Inactive coordinates become active if they have exactly 3 active neighbors
            # Active coordinates stay active only if they have 2 or 3 active neighbors
            if count == 3 or (count == 2 and coord in active_cells):
                new_active_cells.add(coord)

        active_cells = new_active_cells

    return len(active_cells)


def part2():
    active_cells = set()
    neighbors = get_neighbors(4)
    y = 0
    z = 0
    w = 0

    for line in ms:
        for x, c in enumerate(line):
            if c == "#":
                active_cells.add((x, y, z, w))
        y += 1

    for _ in range(NUM_CYCLES):
        neighbor_count = defaultdict(int)
        new_active_cells = set()

        for cell in active_cells:
            for ni, nj, nk, nl in neighbors:
                neighbor_count[
                    (cell[0] + ni, cell[1] + nj, cell[2] + nk, cell[3] + nl)
                ] += 1

        for coord, count in neighbor_count.items():
            if count == 3 or (count == 2 and coord in active_cells):
                new_active_cells.add(coord)

        active_cells = new_active_cells

    return len(active_cells)


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 388
assert ans_part_2 == 2280
