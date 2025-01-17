from collections import defaultdict
from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()


#              UP      RIGHT   DOWN    LEFT
DIRECTION = [(-1, 0), (0, 1), (1, 0), (0, -1)]


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


def find_less(arr, value):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] < value:
            return arr[i]
    return -1


def find_more(arr, value):
    for i in range(len(arr)):
        if arr[i] > value:
            return arr[i]
    return -1


def part1(ci, cj):
    dir_index = 0
    di, dj = DIRECTION[dir_index]
    visited = set()
    original_path = []

    visited.add((ci, cj))
    while True:
        ni = ci + di
        nj = cj + dj

        if ni >= len(grid) or ni < 0 or nj >= len(grid[0]) or nj < 0:
            break

        grid_val = grid[ni][nj]
        if grid_val == ".":
            visited.add((ni, nj))
            original_path.append((ni, nj, dir_index))
            ci, cj = ni, nj
        elif grid_val == "#":
            dir_index = (dir_index + 1) % 4
            di, dj = DIRECTION[dir_index]

    return len(visited), original_path


def part2(original_path):
    """
    Basic answer is to put obstacle on each point of original guard path
    and check if path is looped.

    1. One optimization, dont start for checking path loop from start but just before
    the obstacle position
    2. Second optimization, only save visited states at turns during loop check
    3. Instead of looping teleport to corners where stones are present
    """
    len_rows = len(grid)
    len_cols = len(grid[0])

    def get_stones_arr():
        stone_hz = defaultdict(list)
        stone_vt = defaultdict(list)

        for i in range(len_rows):
            for j in range(len_cols):
                if grid[i][j] == "#":
                    stone_hz[i].append(j)
                    stone_vt[j].append(i)
        return stone_hz, stone_vt

    def is_path_looped(ci, cj, dir_index):
        visited = set()

        while True:
            # update coordinate to next stone location
            if dir_index == 0:
                ns_loc = find_less(stone_vt[cj], ci)
                ci = ns_loc + 1
            elif dir_index == 1:
                ns_loc = find_more(stone_hz[ci], cj)
                cj = ns_loc - 1
            elif dir_index == 2:
                ns_loc = find_more(stone_vt[cj], ci)
                ci = ns_loc - 1
            else:
                ns_loc = find_less(stone_hz[ci], cj)
                cj = ns_loc + 1

            if ns_loc < 0:
                return False

            if (ci, cj, dir_index) in visited:
                return True

            visited.add((ci, cj, dir_index))
            dir_index = (dir_index + 1) % 4

    stone_hz, stone_vt = get_stones_arr()
    looped_paths = 0
    covered_pt = set()
    for oi, oj, dir in original_path:
        if (oi, oj) in covered_pt:
            continue
        covered_pt.add((oi, oj))

        stone_hz[oi].append(oj)
        stone_vt[oj].append(oi)

        # sort them
        stone_hz[oi].sort()
        stone_vt[oj].sort()

        a = oi - DIRECTION[dir][0]
        b = oj - DIRECTION[dir][1]
        if is_path_looped(a, b, dir):
            looped_paths += 1

        stone_hz[oi].remove(oj)
        stone_vt[oj].remove(oi)

    return looped_paths


grid, si, sj = initialize_grid()

part1_ans, original_path = part1(si, sj)
part2_ans = part2(original_path)

print("Part1 solution: ", part1_ans)
print("Part2 solution: ", part2_ans)

assert part1_ans == 5177
assert part2_ans == 1686
