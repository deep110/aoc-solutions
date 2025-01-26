import re
from aoc.utils import read_input

PATTERN = re.compile(r"(\d+),(\d+)")


def parse_input():
    ms = read_input(2022, 14).split("\n")
    y_max = -1
    rock_paths = []

    for i in ms:
        rkp = i.split(" -> ")
        a = []
        for r in rkp:
            m = r.split(",")
            yp = int(m[1])
            a.append((int(m[0]), yp))
            if yp > y_max:
                y_max = yp
        rock_paths.append(a)
    return rock_paths, y_max


def initialize_grid(_paths):
    size = 750
    grid = [["."] * size for i in range(200)]

    for rkp in _paths:
        for a, b in zip(rkp, rkp[1:]):
            if a[0] == b[0]:
                sign = 1 if a[1] < b[1] else -1
                for k in range(a[1], b[1] + sign, sign):
                    grid[k][a[0]] = "#"
            else:
                sign = 1 if a[0] < b[0] else -1
                for k in range(a[0], b[0] + sign, sign):
                    grid[a[1]][k] = "#"

    return grid


def part1():
    grid = initialize_grid(rock_paths)

    sand_num = 0
    infinite_fall = False
    while not infinite_fall:
        s_pos = [0, 500]
        is_rest = False
        while not is_rest:
            if s_pos[0] > y_max:
                infinite_fall = True
                break

            if grid[s_pos[0] + 1][s_pos[1]] == ".":
                s_pos[0] += 1
            elif grid[s_pos[0] + 1][s_pos[1] - 1] == ".":
                s_pos[0] += 1
                s_pos[1] -= 1
            elif grid[s_pos[0] + 1][s_pos[1] + 1] == ".":
                s_pos[0] += 1
                s_pos[1] += 1
            else:
                grid[s_pos[0]][s_pos[1]] = "o"
                is_rest = True
                sand_num += 1

    return sand_num, grid


def part2(grid, start_sand_num):
    sand_num = start_sand_num
    blocked = False

    while not blocked:
        if grid[0][500] == "o":
            blocked = True
            break

        s_pos = [0, 500]
        is_rest = False
        while not is_rest:
            if s_pos[0] == y_max + 1:
                grid[y_max + 1][s_pos[1]] = "o"
                is_rest = True
                sand_num += 1
            elif grid[s_pos[0] + 1][s_pos[1]] == ".":
                s_pos[0] += 1
            elif grid[s_pos[0] + 1][s_pos[1] - 1] == ".":
                s_pos[0] += 1
                s_pos[1] -= 1
            elif grid[s_pos[0] + 1][s_pos[1] + 1] == ".":
                s_pos[0] += 1
                s_pos[1] += 1
            else:
                grid[s_pos[0]][s_pos[1]] = "o"
                is_rest = True
                sand_num += 1

    return sand_num


rock_paths, y_max = parse_input()

ans_part_1, _grid = part1()
ans_part_2 = part2(_grid, ans_part_1)

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 638
assert ans_part_2 == 31722
