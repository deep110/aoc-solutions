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
from dataclasses import dataclass
from typing import List
from aoc.utils import read_input


@dataclass
class Tile:
    id: int
    data: List[str]
    edges: List[str]

    @classmethod
    def from_string(cls, input_str):
        rows = input_str.split("\n")
        tile_id = int(rows[0][5:9])

        return Tile(id=tile_id, data=rows[1:], edges=[])

    def read_edges(self):
        # top and bottom edge is easy
        self.edges.extend(
            [self.data[0], self.data[0][::-1], self.data[-1], self.data[-1][::-1]]
        )
        len_tile = len(self.data)

        # left and right
        left = []
        right = []
        for i in range(len_tile):
            left.append(self.data[i][0])
            right.append(self.data[i][len_tile - 1])
        left = "".join(left)
        right = "".join(right)
        self.edges.extend(
            [
                left,
                left[::-1],
                right,
                right[::-1],
            ]
        )

        return self.edges


ms = read_input(2020, 20).split("\n\n")
# ms = test.split("\n\n")
tiles: List[Tile] = [Tile.from_string(m) for m in ms]


def part1():
    result = 1
    edge_frequency = defaultdict(int)
    for tile in tiles:
        for edge in tile.read_edges():
            edge_frequency[edge] += 1

    for tile in tiles:
        edges = tile.edges
        # only count edges of one orientation
        freq_sum = (
            edge_frequency[edges[0]]
            + edge_frequency[edges[2]]
            + edge_frequency[edges[4]]
            + edge_frequency[edges[6]]
        )

        if freq_sum == 6:
            result *= tile.id
    return result


def part2():
    pass


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 15003787688423
# assert ans_part_2 == 0
