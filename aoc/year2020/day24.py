"""
# Lobby Layout

I am using [Axial Coordinate System](https://www.redblobgames.com/grids/hexagons/#coordinates-axial) for
hex parsing and navigation.

For Part2, it is repeat of day 17.
"""

from collections import defaultdict
from aoc.utils import read_input


ms = read_input(2020, 24).split("\n")


def part1():
    black_tiles = set()
    for line in ms:
        q, r = (0, 0)
        i = 0
        while i < len(line):
            match line[i]:
                case "e":
                    q += 1
                case "w":
                    q -= 1
                case "n":
                    if line[i + 1] == "e":
                        q += 1
                        r -= 1
                    else:
                        r -= 1
                    i += 1
                case "s":
                    if line[i + 1] == "e":
                        r += 1
                    else:
                        q -= 1
                        r += 1
                    i += 1
            i += 1

        tile = (q, r)
        if tile in black_tiles:
            black_tiles.remove(tile)
        else:
            black_tiles.add(tile)

    return len(black_tiles), black_tiles


def part2(black_tiles):
    #              e        w       ne       nw        se      sw
    neighbors = [(1, 0), (-1, 0), (1, -1), (0, -1), (0, 1), (-1, 1)]
    active_cells = black_tiles
    next_active_cells = set()

    for _ in range(100):
        neighbor_count = defaultdict(int)

        for cq, cr in active_cells:
            for nq, nr in neighbors:
                neighbor_count[(cq + nq, cr + nr)] += 1

        next_active_cells.clear()

        for coord, count in neighbor_count.items():
            if count == 2 or (count == 1 and coord in active_cells):
                next_active_cells.add(coord)

        active_cells, next_active_cells = next_active_cells, active_cells

    return len(active_cells)


ans_part_1, black_tiles = part1()
ans_part_2 = part2(black_tiles)

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 386
assert ans_part_2 == 4214
