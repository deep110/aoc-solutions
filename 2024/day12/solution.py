from os import path
from typing import List


class Region:
    def __init__(self, value):
        self.value = value
        self.perimeter = 0
        self.area = 1
        self.corners = 0


with open(path.join(path.dirname(__file__), "input.txt")) as f:
    garden = list(map(lambda x: x.strip(), f.readlines()))

#              UP,     RIGHT,   DOWN,     LEFT
DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
DIAGONALS = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
NUM_ROWS = len(garden)
NUM_COLUMNS = len(garden[0])


def fill_region(start, region: Region, visited: List[bool]):
    """
    Area : num of points is area
    Perimeter: number of boundary sides, is perimeter
    Sides: Number of corners, both interior and exterior
    """
    stack = [start]
    neighbors_in_region = [False] * 4

    while stack:
        si, sj = stack.pop()

        for idx, (di, dj) in enumerate(DIRECTIONS):
            ni, nj = si + di, sj + dj

            if (
                ni < 0
                or ni >= NUM_ROWS
                or nj < 0
                or nj >= NUM_COLUMNS
                or garden[ni][nj] != region.value
            ):
                neighbors_in_region[idx] = False
                region.perimeter += 1
                continue

            neighbors_in_region[idx] = True
            idx = ni + nj * NUM_ROWS
            if not visited[idx]:
                region.area += 1
                visited[idx] = True
                stack.append((ni, nj))

        # count corners
        for idx in range(4):
            idx_next = (idx + 1) % 4

            # external / convex corners
            if (not neighbors_in_region[idx]) and (not neighbors_in_region[idx_next]):
                region.corners += 1

            # internal / concave corners
            if neighbors_in_region[idx] and neighbors_in_region[idx_next]:
                dag_i, dag_j = DIAGONALS[idx]
                if garden[si + dag_i][sj + dag_j] != region.value:
                    region.corners += 1


def part12():
    # We need to iterate over whole garden and create regions, using DFS
    price = 0
    price_discounted = 0
    visited = [False] * (NUM_ROWS * NUM_COLUMNS)
    for i in range(NUM_ROWS):
        for j in range(NUM_COLUMNS):
            idx = i + j * NUM_ROWS
            if visited[idx]:
                continue

            visited[idx] = True

            # create region with default area of 1
            region = Region(garden[i][j])
            fill_region((i, j), region, visited)

            price += region.area * region.perimeter
            price_discounted += region.area * region.corners

    return price, price_discounted


ans_part_1, ans_part_2 = part12()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 1518548
assert ans_part_2 == 909564
