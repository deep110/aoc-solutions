from collections import defaultdict
from itertools import product
from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

NUM_CYCLES = 6
ms = list(map(lambda x: x.strip(), ms))


def get_neighbors(dimension: int):
    offsets = [-1, 0, 1]
    neighbors = list(product(offsets, repeat=dimension))
    neighbors.remove((0,) * dimension)
    return neighbors


def part1():
    coord_dict = {}
    neighbors = get_neighbors(3)
    y = 0
    z = 0

    for line in ms:
        for x, c in enumerate(line):
            coord_dict[(x, y, z)] = c == "#"
        y += 1

    for _ in range(NUM_CYCLES):
        neighbor_count = defaultdict(int)
        n_map = {}

        # Find each active coordinate, and for each of its neighbor add 1
        # We are doing reverse, instead of looping on each coordinate and finding active neighbors, we are
        # looking into each active coordinate and adding 1 to each neighbor.
        for c in coord_dict:
            if coord_dict[c]:
                for ni, nj, nk in neighbors:
                    neighbor_count[(c[0] + ni, c[1] + nj, c[2] + nk)] += 1

        for this_coord in neighbor_count:
            # If the coord is newly viewed, then its initial state must be inactive
            try:
                current_state = coord_dict[this_coord]
            except KeyError:
                current_state = False

            # Active coordinates stay active only if they have 2 or 3 active neighbors
            if current_state and not (2 <= neighbor_count[this_coord] <= 3):
                n_map[this_coord] = False
            # Inactive coordinates become active if they have exactly 3 active neighbors
            elif not current_state and neighbor_count[this_coord] == 3:
                n_map[this_coord] = True
            else:
                n_map[this_coord] = current_state

        coord_dict = n_map

    return sum(coord_dict.values())


def part2():
    coord_dict = {}
    neighbors = get_neighbors(4)
    y = 0
    z = 0
    w = 0

    for line in ms:
        for x, c in enumerate(line):
            coord_dict[(x, y, z, w)] = c == "#"
        y += 1

    for _ in range(NUM_CYCLES):
        neighbor_count = defaultdict(int)
        n_map = {}

        for c in coord_dict:
            if coord_dict[c]:
                for ni, nj, nk, nl in neighbors:
                    neighbor_count[(c[0] + ni, c[1] + nj, c[2] + nk, c[3] + nl)] += 1

        for this_coord in neighbor_count:
            try:
                current_state = coord_dict[this_coord]
            except KeyError:
                current_state = False

            if current_state and not (2 <= neighbor_count[this_coord] <= 3):
                n_map[this_coord] = False
            elif not current_state and neighbor_count[this_coord] == 3:
                n_map[this_coord] = True
            else:
                n_map[this_coord] = current_state

        coord_dict = n_map

    return sum(coord_dict.values())


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 388
assert ans_part_2 == 2280
