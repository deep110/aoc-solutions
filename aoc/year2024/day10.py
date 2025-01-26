from typing import List, Set
from aoc.utils import read_input

ms = read_input(2024, 10).split("\n")

grid = list(map(lambda x: list(map(lambda x: int(x), x)), ms))
NUM_ROWS = len(grid)
NUM_COLUMNS = len(grid[0])


def part1():
    def count_trail_head_score(i, j, ends: Set, visited: Set):
        if grid[i][j] == 9:
            ends.add((i, j))
            return

        if (i, j) in visited:
            return
        visited.add((i, j))

        if i < NUM_ROWS - 1 and grid[i + 1][j] - grid[i][j] == 1:
            count_trail_head_score(i + 1, j, ends, visited)

        if i > 0 and grid[i - 1][j] - grid[i][j] == 1:
            count_trail_head_score(i - 1, j, ends, visited)

        if j < NUM_COLUMNS - 1 and grid[i][j + 1] - grid[i][j] == 1:
            count_trail_head_score(i, j + 1, ends, visited)

        if j > 0 and grid[i][j - 1] - grid[i][j] == 1:
            count_trail_head_score(i, j - 1, ends, visited)

    score = 0
    for i in range(NUM_ROWS):
        for j in range(NUM_COLUMNS):
            if grid[i][j] == 0:
                visited = set()
                trail_ends = set()
                count_trail_head_score(i, j, trail_ends, visited)
                score += len(trail_ends)

    return score


def part2():
    def count_trail_head_rating(i, j, ends: List):
        if grid[i][j] == 9:
            ends.append((i, j))
            return

        if i < NUM_ROWS - 1 and grid[i + 1][j] - grid[i][j] == 1:
            count_trail_head_rating(i + 1, j, ends)

        if i > 0 and grid[i - 1][j] - grid[i][j] == 1:
            count_trail_head_rating(i - 1, j, ends)

        if j < NUM_COLUMNS - 1 and grid[i][j + 1] - grid[i][j] == 1:
            count_trail_head_rating(i, j + 1, ends)

        if j > 0 and grid[i][j - 1] - grid[i][j] == 1:
            count_trail_head_rating(i, j - 1, ends)

    score = 0
    for i in range(NUM_ROWS):
        for j in range(NUM_COLUMNS):
            if grid[i][j] == 0:
                trail_ends = []
                count_trail_head_rating(i, j, trail_ends)
                score += len(trail_ends)

    return score


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 461
assert ans_part_2 == 875
