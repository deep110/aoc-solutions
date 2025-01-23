from os import path

DIRECTIONS = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    wires = list(map(lambda x: x.strip().split(","), f.readlines()))


class Wire:
    def __init__(self, ops):
        self.segments = []
        self.previous = (0, 0)
        self.current = (0, 0)

        # transverse
        for op in ops:
            (di, dj), steps = DIRECTIONS[op[:1]], int(op[1:])
            self.current = self.previous[0] + steps * di, self.previous[1] + steps * dj

            self.segments.append((self.previous, self.current))
            self.previous = self.current

    def orientation(self, a, b, c):
        return (c[1] - a[1]) * (b[0] - a[0]) > (b[1] - a[1]) * (c[0] - a[0])

    def do_intersect(self, p1, q1, p2, q2):
        """
        https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/
        """
        return self.orientation(p1, p2, q2) != self.orientation(
            q1, p2, q2
        ) and self.orientation(p1, q1, p2) != self.orientation(p1, q1, q2)

    def intersections(self, grid2: "Wire"):
        intersections = []
        i = 0
        for p1, q1 in self.segments:
            i += abs(p1[0] - q1[0]) + abs(p1[1] - q1[1])
            j = 0
            for p2, q2 in grid2.segments:
                j += abs(p2[0] - q2[0]) + abs(p2[1] - q2[1])
                if self.do_intersect(p1, q1, p2, q2):
                    steps = i + j

                    # Assumes no co-linearity (intersections are always orthogonal)
                    if p1[0] == q1[0]:
                        # Subtract paths from intersection to the end of the segments
                        steps -= abs(q1[1] - p2[1]) + abs(q2[0] - p1[0])
                        intersection = (p1[0], p2[1])
                    else:
                        # Subtract paths from intersection to the end of the segments
                        steps -= abs(q1[0] - p2[0]) + abs(q2[1] - p1[1])
                        intersection = (p1[1], p2[0])

                    intersections.append((intersection, steps))

        return intersections


def part12():
    wire1 = Wire(wires[0])
    wire2 = Wire(wires[1])

    min_dist = 1000000000000
    min_steps = 1000000000000

    for intersection, steps in wire1.intersections(wire2):
        dist = abs(intersection[0]) + abs(intersection[1])
        if dist < min_dist:
            min_dist = dist
        if steps < min_steps:
            min_steps = steps

    return min_dist, min_steps


ans_part_1, ans_part_2 = part12()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 529
assert ans_part_2 == 20386
