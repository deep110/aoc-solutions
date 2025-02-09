"""
# Day 9: Smoke Basin

Part1, is straight forward, no tricks there to reduce the computation.

For Part2, I am using a
"""

from typing import List, Tuple
from aoc.utils import read_input

#              UP      RIGHT   DOWN    LEFT
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

ms = read_input(2021, 9).splitlines()
grid = [[int(x) for x in row] for row in ms]
num_rows = len(grid)
num_columns = len(grid[0])


def flood_fill_bfs(start_i, start_j) -> int:
    """
    Takes start point and flood fills the basin, and returns the size
    """
    stack = [(start_i, start_j)]
    size = 0
    done = set()

    while stack:
        point = stack.pop()
        if point in done:
            continue

        current_i, current_j = point
        value = grid[current_i][current_j]
        done.add(point)

        size += 1
        for di, dj in DIRECTIONS:
            ni, nj = current_i + di, current_j + dj
            if ni < 0 or ni >= num_rows or nj < 0 or nj >= num_columns:
                continue
            if grid[ni][nj] != 9 and grid[ni][nj] > value:
                stack.append((ni, nj))

    return size


def part1():
    total_risk_level = 0
    low_points = []
    for i in range(num_rows):
        for j in range(num_columns):
            value = grid[i][j]
            is_low = True

            for di, dj in DIRECTIONS:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= num_rows or nj < 0 or nj >= num_columns:
                    continue

                if value >= grid[ni][nj]:
                    is_low = False
                    break

            if is_low:
                total_risk_level += value + 1
                low_points.append((i, j))

    return total_risk_level, low_points


def part2(low_points: List[Tuple[int, int]]):
    basins = []

    for si, sj in low_points:
        size = flood_fill_bfs(si, sj)
        basins.append(size)

    basins.sort(reverse=True)
    return basins[0] * basins[1] * basins[2]


ans_part_1, low_points = part1()
ans_part_2 = part2(low_points)

print("Part1 solution:", ans_part_1)
print("Part2 solution:", ans_part_2)

assert ans_part_1 == 498
assert ans_part_2 == 1071000
