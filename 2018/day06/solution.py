from collections import defaultdict
from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()


def manhattan_dist(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])


coords = [tuple(int(s) for s in m.split(", ")) for m in ms]

x_min = min(coords, key=lambda c: c[0])[0]
x_max = max(coords, key=lambda c: c[0])[0]
y_min = min(coords, key=lambda c: c[1])[1]
y_max = max(coords, key=lambda c: c[1])[1]


def part1():
    """
    Idea is to iterate over all the points inside a bounding box:

    1. Mark the point closest to given coordinates.
    2. The criteria for coord region to be marked INFINITE is if any point of that region lies on edge.
    """
    closest_coord_map = dict()

    for i in range(x_min, x_max + 1):
        for j in range(y_min, y_max + 1):
            d = float("inf")
            which_c = None
            can_add = True
            for c in coords:
                man_d = manhattan_dist(c, (i, j))
                if man_d < d:
                    d = man_d
                    which_c = c
                    can_add = True
                elif man_d == d:
                    can_add = False

            if can_add:
                closest_coord_map[(i, j)] = which_c

    inf_coord = []
    coords_areas = defaultdict(int)
    for xy, coord in closest_coord_map.items():
        if coord in inf_coord:
            continue

        if xy[0] in (x_min, x_max) or xy[1] in (y_min, y_max):
            inf_coord.append(coord)
            continue

        coords_areas[coord] += 1

    return max(coords_areas.values())


def part2():
    def sum_points(point, coords):
        p = 0
        for c in coords:
            p += manhattan_dist(point, c)
            if p >= 10000:
                return False
        return True

    desired_area = 0
    for i in range(x_min, x_max + 1):
        for j in range(y_min, y_max + 1):
            if sum_points((i, j), coords):
                desired_area += 1

    return desired_area


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 3620
assert ans_part_2 == 39930
