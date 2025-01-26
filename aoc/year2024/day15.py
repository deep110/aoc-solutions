from typing import List
from aoc.utils import read_input

ms = read_input(2024, 15).split("\n")
map_end_index = ms.index("")

DMAP = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}


def initialize_grid_p1():
    grid = []
    start_pos = None
    for i in range(map_end_index):
        if not start_pos and "@" in ms[i]:
            start_pos = (i, ms[i].index("@"))
        grid.append(list(ms[i]))

    grid[start_pos[0]][start_pos[1]] = "."
    return grid, start_pos


def initialize_grid_p2():
    REPLACE = {
        "#": ["#", "#"],
        ".": [".", "."],
        "@": [".", "."],
        "O": ["[", "]"],
        "\n": [],
    }

    grid = []
    start_pos = None
    for i in range(map_end_index):
        row = []
        for j in range(len(ms[i])):
            row.extend(REPLACE[ms[i][j]])
            if not start_pos and ms[i][j] == "@":
                start_pos = (i, int(j * 2))
        grid.append(row)

    return grid, start_pos


def part1():
    """
    In moving box, one trick of optimizing is just teleport the box to first free
    position we find. Its equivalent of shifting all the boxes.
    """
    grid, start_pos = initialize_grid_p1()
    directions = "".join(ms[map_end_index + 1 :])

    def get_new_box_position(move_dir, box_pos):
        mi, mj = box_pos

        while True:
            mi, mj = mi + move_dir[0], mj + move_dir[1]
            if grid[mi][mj] == ".":
                return (mi, mj)
            elif grid[mi][mj] == "#":
                return None

    ri, rj = start_pos
    for sdir in directions:
        dir = DMAP[sdir]
        ni, nj = ri + dir[0], rj + dir[1]

        if grid[ni][nj] == ".":
            ri, rj = ni, nj
        elif grid[ni][nj] == "O":
            if new_box_pos := get_new_box_position(dir, (ni, nj)):
                # shift the box
                grid[new_box_pos[0]][new_box_pos[1]] = "O"
                grid[ni][nj] = "."
                # we move to this position
                ri, rj = ni, nj

    gps_sum = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "O":
                gps_sum += 100 * i + j
    return gps_sum


def part2():
    """
    Now for part 2, same trick wont work easily for vertical. A DFS based approach
    would be ideal
    """
    grid, start_pos = initialize_grid_p2()
    directions = "".join(ms[map_end_index + 1 :])
    move_map = {
        "]": -1,
        "[": 1,
    }

    def move_box_hz(rck_i, rck_j, move_dir):
        # old trick works
        mi, mj = rck_i, rck_j
        while True:
            mj += 2 * move_dir[1]
            if grid[mi][mj] == ".":
                if mj < rck_j:
                    grid[mi][mj:rck_j] = grid[mi][mj + 1 : rck_j + 1]
                else:
                    grid[mi][rck_j + 1 : mj + 1] = grid[mi][rck_j:mj]
                grid[rck_i][rck_j] = "."
                return True
            elif grid[mi][mj] == "#":
                return False

    def move_box_vt(mi, mj, move_dir, ops: List):
        val = grid[mi][mj]

        if val == ".":
            return True
        elif val == "#":
            return False

        is_empty = move_box_vt(mi + move_dir[0], mj, move_dir, ops)
        if not is_empty:
            return False

        is_empty = move_box_vt(mi + move_dir[0], mj + move_map[val], move_dir, ops)
        if not is_empty:
            return False

        if val == "[" and (mi, mj) not in ops:
            ops.append((mi, mj))
        elif val == "]" and (mi, mj + move_map[val]) not in ops:
            ops.append((mi, mj + move_map[val]))

        return True

    ri, rj = start_pos
    for sdir in directions:
        dir = DMAP[sdir]
        ni, nj = ri + dir[0], rj + dir[1]

        if grid[ni][nj] == ".":
            ri, rj = ni, nj
        elif grid[ni][nj] in ["[", "]"]:
            if sdir in ["<", ">"]:
                if move_box_hz(ni, nj, dir):
                    ri, rj = ni, nj
            else:
                ops = []
                if move_box_vt(ni, nj, dir, ops):
                    for op in ops:
                        grid[op[0] + dir[0]][op[1] : op[1] + 2] = ["[", "]"]
                        grid[op[0]][op[1] : op[1] + 2] = [".", "."]

                    ri, rj = ni, nj

    gps_sum = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "[":
                gps_sum += 100 * i + j
    return gps_sum


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 1412971
assert ans_part_2 == 1429299
