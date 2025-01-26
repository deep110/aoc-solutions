"""
# Monitoring Station

## Part One
We compare each pair of points, first subtracting the current asteroid to get a relative vector.
Since all coordinates are integers we can check for multiple points on the same line by
reducing the vector by its [greatest common divisor](https://en.wikipedia.org/wiki/Greatest_common_divisor).
For example, looking from the origin `(0, 0)`, the points `(3, 5)`, `(6, 10)` and `(21, 35)`
are all on the same line, with gcds of 1, 2 and 7 respectively.

For each point we build a set of previously seen values. Since we can see at most one asteroid
in a given direction, if a vector is already in the set then we ignore it. The final size of
the set is the number of visible asteroids.

## Part Two

Using atan2 to get the angle, sort them, and pop asteroids one by one in the increasing order of angle.
"""

from collections import defaultdict
import math

from aoc.utils import read_input

TWO_PI = 6.2831

ms = read_input(2019, 10).split("\n")
asteroids = []
for i in range(len(ms)):
    for j in range(len(ms[0])):
        if ms[i][j] == "#":
            asteroids.append((j, i))


def part1():
    max_asteroids = 0
    best_x = best_y = 0

    for x, y in asteroids:
        point_slopes = set()
        for x2, y2 in asteroids:
            if (x, y) != (x2, y2):
                # Calculate relative position
                dx, dy = x2 - x, y2 - y
                # Key insight is that points on the same line are integer multiples of each other.
                # so we remove common divisor
                g = math.gcd(dx, dy)
                point_slopes.add((dx // g, dy // g))

        if len(point_slopes) > max_asteroids:
            max_asteroids = len(point_slopes)
            best_x, best_y = x, y

    return max_asteroids, (best_x, best_y)


def to_angle(x, y):
    """
    converts to angle between 0 to 360 deg, with positive y-axis as 0 and angle
    increases clockwise
    """
    angle_rad = math.atan2(x, y)
    return (TWO_PI + angle_rad) % TWO_PI


def part2(sx, sy):
    asteroids.remove((sx, sy))
    # first map all asteroids to the angle they make with station
    ast_station_angle = defaultdict(list)
    for x, y in asteroids:
        # we have to invert y since, atan2 considers positive y upside, but in our coordinate
        # y decreases as we move up
        angle = to_angle(x - sx, sy - y)
        ast_station_angle[angle].append((x, y))

    # sort out every asteroid by manhattan distance in their group
    for angle in ast_station_angle:
        ast_station_angle[angle].sort(
            key=lambda c: abs(c[0] - sx) + abs(c[1] - sy), reverse=True
        )

    # sort the dict angles
    order = list(ast_station_angle.keys())
    order.sort()

    # now iterate over and blast the asteroids
    len_order = len(order)
    idx = 0
    num_found = 0
    while num_found < 200:
        k = ast_station_angle[order[idx]].pop()
        num_found += 1
        idx = (idx + 1) % len_order

    return k[0] * 100 + k[1]


ans_part_1, (station_x, station_y) = part1()
ans_part_2 = part2(station_x, station_y)

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 230
assert ans_part_2 == 1205
