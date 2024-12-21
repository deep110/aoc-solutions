from os import path

#              UP      RIGHT   DOWN    LEFT
DIRECTION = [(-1, 0), (0, 1), (1, 0), (0, -1)]

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

grid = list(map(lambda x: list(x.strip()), ms))
start_position = (len(grid) - 2, 1, DIRECTION[1])
end_position = (1, len(grid) - 2, None)


def a_star_search(grid, start, end, heuristic_func, cost_func):
    # Initialize open and closed sets
    open_set = set()
    closed_set = set()

    # Add start node to open set
    open_set.add(start)

    # Dictionary to store parent nodes for each node
    came_from = {}

    # Dictionary to store the cost from start to each node
    g_score = {start: 0}

    # Dictionary to store the estimated total cost (g_score + heuristic)
    f_score = {start: heuristic_func(start, end)}

    while open_set:
        # Find the node in open set with the lowest f_score
        current = min(open_set, key=lambda x: f_score[x])

        # Check if we have reached the end
        if current[:2] == end[:2]:
            # print("path found", current)
            unique_tiles = set()
            reconstruct_path(came_from, current, unique_tiles)
            return g_score[current], unique_tiles

        open_set.remove(current)
        closed_set.add(current)

        for neighbor in get_neighbors(grid, current):
            # Calculate tentative g_score for neighbor
            tentative_g_score = g_score[current] + cost_func(current, neighbor)

            # Check if neighbor is in closed set or if tentative g_score is worse than current g_score
            # we already have a path that is better than this
            g_score_neigh = g_score.get(neighbor, float("inf"))

            # handle case for part2
            if tentative_g_score == g_score_neigh:
                if neighbor in open_set or neighbor in closed_set:
                    came_from[neighbor].append(current)

            if neighbor in closed_set and tentative_g_score >= g_score_neigh:
                continue

            # If neighbor is not in open set or tentative g_score is better than current g_score
            if neighbor not in open_set or tentative_g_score < g_score_neigh:
                came_from[neighbor] = [current]
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic_func(neighbor, end)
                open_set.add(neighbor)

    return 0, None


def reconstruct_path(came_from, current, path: set):
    path.add(current[:2])
    for _next in came_from.get(current, []):
        reconstruct_path(came_from, _next, path)


def get_neighbors(grid, node):
    """
    Returns the valid neighbors of a node in the grid, in this case not walls
    """
    i, j, _ = node

    neighbors = []
    for d in DIRECTION:
        ni, nj = i + d[0], j + d[1]
        if grid[ni][nj] != "#":
            neighbors.append((ni, nj, d))

    return neighbors


# lets use manhattan distance
def heuristic(node, end):
    return abs(node[0] - end[0]) + abs(node[1] - end[1])


def cost(node1, node2):
    if node1[2] == node2[2]:
        return 1
    else:
        return 1001


def part12():
    """
    It is a classic path finding problem
    """
    assert grid[start_position[0]][start_position[1]] == "S"
    assert grid[end_position[0]][end_position[1]] == "E"

    path = a_star_search(
        grid, start_position, end_position, heuristic_func=heuristic, cost_func=cost
    )

    return path[0], len(path[1])


ans_part_1, ans_part_2 = part12()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 91464
assert ans_part_2 == 494
