from heapq import heappush, heappop
from os import path
from typing import Dict, List

#              UP      RIGHT   DOWN    LEFT
DIRECTION = [(-1, 0), (0, 1), (1, 0), (0, -1)]

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

grid = list(map(lambda x: list(x.strip()), ms))
start_position = (len(grid) - 2, 1, DIRECTION[1])
end_position = (1, len(grid) - 2, None)


def get_neighbors(grid, node):
    i, j, _ = node
    neighbors = []
    for d in DIRECTION:
        ni, nj = i + d[0], j + d[1]
        if grid[ni][nj] != "#":
            neighbors.append((ni, nj, d))

    return neighbors


def cost(node1, node2):
    if node1[2] == node2[2]:
        return 1
    else:
        return 1001


# we are not using heuristic since it is not adding much value
def a_star_search(grid, start, end):
    # Initialize open and closed sets
    open_set = set()
    closed_set = set()

    # Add start node to open set
    open_set.add(start)

    came_from: Dict[str, List] = {}
    g_score = {start: 0}
    end_coord = end[:2]

    while open_set:
        # Find the node in open set with the lowest score
        current = min(open_set, key=lambda x: g_score[x])

        # Check if we have reached the end
        if current[:2] == end_coord:
            unique_tiles = set()
            reconstruct_path(came_from, current, unique_tiles)
            return g_score[current], unique_tiles

        open_set.remove(current)
        closed_set.add(current)

        for neighbor in get_neighbors(grid, current):
            new_g_score = g_score[current] + cost(current, neighbor)
            old_g_score = g_score.get(neighbor, float("inf"))

            # handle case for part2
            if new_g_score == old_g_score:
                if neighbor in open_set or neighbor in closed_set:
                    came_from[neighbor].append(current)

            if neighbor in closed_set and new_g_score >= old_g_score:
                continue

            # If neighbor is not in open set or tentative g_score is better than current g_score
            if neighbor not in open_set or new_g_score < old_g_score:
                came_from[neighbor] = [current]
                g_score[neighbor] = new_g_score
                open_set.add(neighbor)

    return 0, None


def reconstruct_path(came_from, current, path: set):
    path.add(current[:2])
    for _next in came_from.get(current, []):
        reconstruct_path(came_from, _next, path)


def part12():
    assert grid[start_position[0]][start_position[1]] == "S"
    assert grid[end_position[0]][end_position[1]] == "E"

    min_cost, path = a_star_search(grid, start_position, end_position)

    return min_cost, len(path)


ans_part_1, ans_part_2 = part12()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 91464
assert ans_part_2 == 494
