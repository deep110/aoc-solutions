"""
# Jurassic Jigsaw

## Part1

First we calculate the frequency of each edge, both forwards and backwards as tiles can be in
any orientation. Then for every tile we sum the frequency of each edge.

Corner tiles will have two edges that only occur once, not matching with any other tile,
for a total of 1 + 1 + 2 + 2 = 6.
Other edge tiles have a total of 1 + 2 + 2 + 2 = 7 and
inner tiles a total of 2 + 2 + 2 + 2 = 8
"""

from collections import defaultdict
import re
from typing import Dict, List
from aoc.utils import read_input

TOP, RIGHT, BOTTOM, LEFT = range(4)
MONSTER = [
    "..................#.",
    "#....##....##....###",
    ".#..#..#..#..#..#...",
]
# a) flip the monster to look for more specific match
# b) lookahead to capture overlapping matches
MONSTER_RE1 = re.compile(f"(?=({MONSTER[2]}))")
MONSTER_RE2 = re.compile(MONSTER[1])
MONSTER_RE3 = re.compile(MONSTER[0])


def flip(grid):
    return tuple(row[::-1] for row in grid)


def rotate(grid):
    return tuple("".join(c[::-1]) for c in zip(*grid))


class Tile:
    def __init__(self, id: int, data: List[str]):
        self.id = id
        self.data = data
        self.edges: List[str] = None
        self.frequency = 0

    @classmethod
    def from_string(cls, input_str):
        rows = input_str.split("\n")
        tile = Tile(int(rows[0][5:9]), rows[1:])
        tile.update_edges()
        return tile

    def update_edges(self):
        # left and right
        left = []
        right = []
        for i in range(len(self.data)):
            left.append(self.data[i][0])
            right.append(self.data[i][-1])
        left = "".join(left)
        right = "".join(right)
        self.edges = [
            self.data[0],  # top
            right,  # right
            self.data[-1],  # bottom
            left,  # left
            self.data[0][::-1],
            right[::-1],
            self.data[-1][::-1],
            left[::-1],
        ]

    def get_adjoining_tile(self, tiles_edge: List["Tile"]):
        return tiles_edge[1] if tiles_edge[0].id == self.id else tiles_edge[0]

    # we always rotate clockwise
    def rotate(self):
        self.data = list("".join(c[::-1]) for c in zip(*self.data))
        self.update_edges()

    def flip(self):
        self.data = list(row[::-1] for row in self.data)
        self.update_edges()

    def align_tile(self, edge: str, target_edge_id):
        rotate_count = 0
        while self.edges.index(edge) != target_edge_id:
            if rotate_count == 4:
                self.flip()
                rotate_count = 0

            self.rotate()
            rotate_count += 1

    def inner_data(self):
        return [line[1:-1] for line in self.data[1:-1]]

    def __repr__(self):
        return str(self.id)


ms = read_input(2020, 20).split("\n\n")
tiles: List[Tile] = [Tile.from_string(m) for m in ms]


def get_top_left_tile(tiles: List[Tile], edge_frequency: Dict[str, int]):
    req_tile = None
    for tile in tiles:
        if tile.frequency == 6:
            req_tile = tile
            break

    while True:
        if (
            edge_frequency[req_tile.edges[TOP]]
            == edge_frequency[req_tile.edges[LEFT]]
            == 1
        ):
            break
        req_tile.rotate()
    return req_tile


def count_monsters(img):
    count = 0
    for first, second, third in zip(img[:-2], img[1:-1], img[2:]):
        for match in MONSTER_RE1.finditer(first):
            # zero width match due to lookahead searching
            start = match.span()[0]
            end = start + 20
            if MONSTER_RE2.match(second[start:end]) and MONSTER_RE3.match(
                third[start:end]
            ):
                count += 1
    return count


def part1():
    result = 1
    # keeping count of every edge
    edge_frequency = defaultdict(int)
    edge_to_tile = defaultdict(list)
    for tile in tiles:
        for edge in tile.edges:
            edge_frequency[edge] += 1
            edge_to_tile[edge].append(tile)

    for tile in tiles:
        edges = tile.edges
        # only count edges of one orientation
        tile.frequency = (
            edge_frequency[edges[0]]
            + edge_frequency[edges[1]]
            + edge_frequency[edges[2]]
            + edge_frequency[edges[3]]
        )
        if tile.frequency == 6:
            result *= tile.id
    return result, edge_frequency, edge_to_tile


def part2(edge_frequency: Dict[str, int], edge_to_tile: Dict[str, List[Tile]]):
    # Now we assemble the tiles into image which is 2D array of tiles
    #
    # We start with a corner tile and find matching tiles for its shared edges
    # If we do this recursively, we will have our image
    aligned_tiles: List[List[Tile]] = []

    # start with top-left corner tile
    current = get_top_left_tile(tiles, edge_frequency)
    while True:
        row = [current]
        # edges are stored in clockwise order, starting from top
        # first process right side tiles
        while True:
            edge = current.edges[RIGHT]
            if edge_frequency[edge] != 2:
                break

            # Next's tile left edge should match current tile's right
            current = current.get_adjoining_tile(edge_to_tile[edge])
            current.align_tile(edge, LEFT)
            row.append(current)

        aligned_tiles.append(row)

        # move to bottom row
        bottom_edge = row[0].edges[BOTTOM]
        if edge_frequency[bottom_edge] != 2:
            break
        current = row[0].get_adjoining_tile(edge_to_tile[bottom_edge])
        current.align_tile(bottom_edge, TOP)

    image = []
    for row in aligned_tiles:
        inners_row = list(tile.inner_data() for tile in row)
        image.extend(map("".join, zip(*inners_row)))

    for rotation in range(8):
        if monster_count := count_monsters(image):
            water = sum(row.count("#") for row in image)
            monster = sum(row.count("#") for row in MONSTER)
            return water - monster * monster_count
        if rotation == 4:
            image = flip(image)
        else:
            image = rotate(image)


ans_part_1, edge_frequency, edge_to_tile = part1()
ans_part_2 = part2(edge_frequency, edge_to_tile)

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 15003787688423
assert ans_part_2 == 1705
