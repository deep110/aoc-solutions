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
    """
    covered_pt = set()
    len_rows = len(grid)
    len_cols = len(grid[0])

    def is_path_looped(ci, cj, _curr_dir):
        dir_index = _curr_dir
        di, dj = DIRECTION[dir_index]
        visited = set()
        visited.add((ci, cj, dir_index))
        dir_changed = False

        while True:
            ni = ci + di
            nj = cj + dj

            if ni >= len_rows or ni < 0 or nj >= len_cols or nj < 0:
                return False
            if (ni, nj, dir_index) in visited:
                return True

            grid_val = grid[ni][nj]
            if grid_val == ".":
                if dir_changed:
                    visited.add((ni, nj, dir_index))
                    dir_changed = False
                ci, cj = ni, nj
            elif grid_val == "#":
                dir_index = (dir_index + 1) % 4
                di, dj = DIRECTION[dir_index]
                dir_changed = True

    looped_paths = 0
    for oi, oj, dir in original_path:
        if (oi, oj) in covered_pt:
            continue
        covered_pt.add((oi, oj))
        grid[oi][oj] = "#"

        a = oi - DIRECTION[dir][0]
        b = oj - DIRECTION[dir][1]
        if is_path_looped(a, b, dir):
            looped_paths += 1
        grid[oi][oj] = "."

    return looped_paths


grid, si, sj = initialize_grid()

part1_ans, original_path = part1(si, sj)
part2_ans = part2(original_path)

print("Part1 solution: ", part1_ans)
print("Part2 solution: ", part2_ans)

assert part1_ans == 5177
assert part2_ans == 1686
