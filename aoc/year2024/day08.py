from collections import defaultdict
from itertools import combinations

from aoc.utils import read_input


def parse_antennas(_grid):
    _antennas = defaultdict(list)
    for i in range(len(_grid)):
        for j in range(len(_grid[i])):
            if _grid[i][j] not in [".", "#"]:
                _antennas[_grid[i][j]].append((i, j))

    return _antennas


def part1():
    anti_nodes = set()
    len_rows = len(grid)
    len_cols = len(grid[0])

    for nodes in antennas.values():
        for a1, a2 in combinations(nodes, 2):
            dir_i = a1[0] - a2[0]
            dir_j = a1[1] - a2[1]

            ai, aj = a1[0] + dir_i, a1[1] + dir_j
            if ai >= 0 and ai < len_rows and aj >= 0 and aj < len_cols:
                anti_nodes.add((ai, aj))

            ai, aj = a2[0] - dir_i, a2[1] - dir_j
            if ai >= 0 and ai < len_rows and aj >= 0 and aj < len_cols:
                anti_nodes.add((ai, aj))

    return len(anti_nodes)


def part2():
    anti_nodes = set()
    len_rows = len(grid)
    len_cols = len(grid[0])

    for nodes in antennas.values():
        for a, b in combinations(nodes, 2):
            dir_i = a[0] - b[0]
            dir_j = a[1] - b[1]

            alpha = 0
            while True:
                ci, cj = a[0] + alpha * dir_i, a[1] + alpha * dir_j
                if ci >= 0 and ci < len_rows and cj >= 0 and cj < len_cols:
                    anti_nodes.add((ci, cj))
                    alpha += 1
                else:
                    break

            beta = 0
            while True:
                ci, cj = b[0] - beta * dir_i, b[1] - beta * dir_j
                if ci >= 0 and ci < len_rows and cj >= 0 and cj < len_cols:
                    anti_nodes.add((ci, cj))
                    beta += 1
                else:
                    break

    return len(anti_nodes)


grid = read_input(2024, 8).split("\n")
antennas = parse_antennas(grid)

ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 259
assert ans_part_2 == 927
