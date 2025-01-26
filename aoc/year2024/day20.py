from aoc.utils import read_input

#              UP      RIGHT   DOWN    LEFT
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


maze = read_input(2024, 20).split("\n")


def parse_input():
    start = None
    end = None

    for i, m in enumerate(maze):
        if not start and "S" in m:
            start = (i, m.index("S"))
        if not end and "E" in m:
            end = (i, m.index("E"))

    return start, end


def find_path():
    # write a simple BFS, since there is just one path, we dont even need to store visited
    path = [start]
    current = start
    prev = None

    while current != end:
        ci, cj = current

        for di, dj in DIRECTIONS:
            _next = ci + di, cj + dj

            if maze[_next[0]][_next[1]] == "#" or _next == prev:
                continue

            path.append(_next)
            prev = current
            current = _next
            break

    return path


def part12_alt():
    cheats_p1 = 0
    cheats_p2 = 0
    path = find_path()
    len_path = len(path)

    for i, (ir, ic) in enumerate(path):
        # no point in checking anything before this point
        j = i + 100
        while j < len_path:
            jr, jc = path[j]

            dist = abs(jr - ir) + abs(jc - ic)

            if dist < 21 and j - i - dist >= 100:
                if dist == 2:
                    cheats_p1 += 1

                cheats_p2 += 1
            elif dist > 20:
                # we can jup ahead by at least this much
                j += dist - 20
                continue

            j += 1

    return cheats_p1, cheats_p2


start, end = parse_input()
ans_part_1, ans_part_2 = part12_alt()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 1438
assert ans_part_2 == 1026446
