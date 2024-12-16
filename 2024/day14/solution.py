import re
from os import path

PATTERN = re.compile(r"p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)")
LEN_X = 101
LEN_Y = 103

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

ms = list(map(lambda x: tuple(int(s) for s in PATTERN.match(x).groups()), ms))


def print_grid(robots):
    grid = []
    for i in range(LEN_Y):
        grid.append(["."] * LEN_X)

    for r in robots:
        grid[r[0][1]][r[0][0]] = "#"

    for r in grid:
        print("".join(r))

    print()


def variance(robots):
    # find mean first
    mean_x = 0
    mean_y = 0
    for r in robots:
        mean_x += r[0][0]
        mean_y += r[0][1]

    mean_x = mean_x / len(robots)
    mean_y = mean_y / len(robots)

    var_x = 0
    var_y = 0
    for r in robots:
        var_x += abs(r[0][0] - mean_x)
        var_y += abs(r[0][1] - mean_y)

    return (var_x / (len(robots) * mean_x), var_y / (len(robots) * mean_y))


def part1():
    robots = []
    for r in ms:
        robots.append((list(r[:2]), list(r[2:])))

    total_time = 100

    for r in robots:
        r[0][0] = (r[0][0] + total_time * r[1][0]) % LEN_X
        r[0][1] = (r[0][1] + total_time * r[1][1]) % LEN_Y

    h_x = LEN_X // 2
    h_y = LEN_Y // 2

    quads = [0, 0, 0, 0]

    for r in robots:
        pos = r[0]
        if pos[0] > h_x:
            if pos[1] > h_y:
                quads[0] += 1
            elif pos[1] < h_y:
                quads[1] += 1
        elif pos[0] < h_x:
            if pos[1] > h_y:
                quads[2] += 1
            elif pos[1] < h_y:
                quads[3] += 1

    return quads[0] * quads[1] * quads[2] * quads[3]


def part2_unoptimized():
    def is_christmas_tree(robots):
        # check for horizontal lines
        grid = []
        for i in range(LEN_Y):
            grid.append(["."] * LEN_X)

        for r in robots:
            grid[r[0][1]][r[0][0]] = "#"

        num_hz = 0
        for v in grid:
            vs = "".join(v)
            if "#####" in vs:
                num_hz += 1

            if num_hz > 6:
                return True

        return False

    robots = []
    for r in ms:
        robots.append((list(r[:2]), list(r[2:])))

    total_time = 0
    while True:
        for r in robots:
            r[0][0] = (r[0][0] + r[1][0]) % LEN_X
            r[0][1] = (r[0][1] + r[1][1]) % LEN_Y

        total_time += 1
        if is_christmas_tree(robots):
            # print_grid(robots)
            break

    return total_time


def part2():
    """
    Since x-axis and y-axis position repeat after every 101 and 103 steps, we have to find at which step
    number horizontal occur and vertical occur
    ```
    x_offset = N % 101
    y_offset = N % 103
    ```
    """
    robots = []
    for r in ms:
        robots.append((list(r[:2]), list(r[2:])))

    tx_offset = 0
    ty_offset = 0
    for t in range(103):
        for r in robots:
            r[0][0] = (r[0][0] + r[1][0]) % LEN_X
            r[0][1] = (r[0][1] + r[1][1]) % LEN_Y

        var_x, var_y = variance(robots)
        if var_x < 0.35:
            tx_offset = t

        if var_y < 0.35:
            ty_offset = t

    # robots = []
    # for r in ms:
    #     robots.append((list(r[:2]), list(r[2:])))

    total_time = 0
    i = 0
    # one more shortcut to this is chinese remainder theorem, for now this works
    while True:
        T_c = tx_offset + i * 101
        if (T_c - ty_offset) % 103 == 0:
            # add one since that time need to be elapsed
            total_time = T_c + 1
            # for r in robots:
            #     r[0][0] = (r[0][0] + total_time * r[1][0]) % LEN_X
            #     r[0][1] = (r[0][1] + total_time * r[1][1]) % LEN_Y

            # print_grid(robots)
            break

        i += 1

    return total_time


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 222208000
assert ans_part_2 == 7623
