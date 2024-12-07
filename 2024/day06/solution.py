from enum import Enum
from os import path
from datetime import datetime

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    RIGHT = (0, 1)
    LEFT = (0, -1)

    def turn_right(self):
        if self == Direction.UP:
            return Direction.RIGHT
        elif self == Direction.RIGHT:
            return Direction.DOWN
        elif self == Direction.DOWN:
            return Direction.LEFT
        else:
            return Direction.UP


def initialize_grid():
    grid = []
    ci, cj = None, None

    for i in range(len(ms)):
        row = list(ms[i].strip())
        grid.append(row)
        if "^" in row:
            ci, cj = i, row.index("^")

    grid[ci][cj] = "."
    return grid, ci, cj


def part1():
    grid, ci, cj = initialize_grid()
    current_dir = Direction.UP
    visited = set()
    visited.add((ci, cj))

    while True:
        ni = ci + current_dir.value[0]
        nj = cj + current_dir.value[1]

        if ni >= len(grid) or ni < 0 or nj >= len(grid[0]) or nj < 0:
            break

        grid_val = grid[ni][nj]
        if grid_val == ".":
            visited.add((ni, nj))
            ci, cj = ni, nj
        elif grid_val == "#":
            current_dir = current_dir.turn_right()

    original_path = list(visited)

    return len(visited), original_path


def part2(original_path):
    grid, si, sj = initialize_grid()

    def walk(ci, cj):
        current_dir = Direction.UP
        visited = set()
        visited.add((ci, cj, current_dir))
        len_rows = len(grid)
        len_cols = len(grid[0])

        while True:
            ni = ci + current_dir.value[0]
            nj = cj + current_dir.value[1]

            if ni >= len_rows or ni < 0 or nj >= len_cols or nj < 0:
                return False
            if (ni, nj, current_dir) in visited:
                return True

            grid_val = grid[ni][nj]
            if grid_val == ".":
                visited.add((ni, nj, current_dir))
                ci, cj = ni, nj
            elif grid_val == "#":
                current_dir = current_dir.turn_right()

    looped_paths = 0
    for p in original_path:
        grid[p[0]][p[1]] = "#"
        if walk(si, sj):
            looped_paths += 1
        grid[p[0]][p[1]] = "."

    return looped_paths


part1_ans, original_path = part1()

print("Part1 solution: ", part1_ans)
print("Part2 solution: ", part2(original_path))
