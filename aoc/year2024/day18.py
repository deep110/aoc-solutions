from aoc.utils import read_input

ms = read_input(2024, 18).split("\n")
total_bytes = list(map(lambda x: tuple(int(j) for j in x.split(",")), ms))
GRID_LEN = 70
DIRECTION = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def a_star_search(_walls, start, end):
    open_set = set()
    closed_set = set()

    open_set.add(start)

    g_score = {start: 0}

    while open_set:
        # Find the node in open set with the lowest f_score
        current = min(open_set)

        # Check if we have reached the end
        if current == end:
            return g_score[current]

        open_set.remove(current)
        closed_set.add(current)

        for neighbor in get_neighbors(_walls, current):
            # no need of cost_func, since it will always be 1
            new_g_score = g_score[current] + 1

            # Check if neighbor is in closed set or if new g_score is worse than current g_score
            old_g_score = g_score.get(neighbor, float("inf"))

            if neighbor in closed_set and new_g_score >= old_g_score:
                continue

            # If neighbor is not in open set or new g_score is better than current g_score
            if neighbor not in open_set or new_g_score < old_g_score:
                g_score[neighbor] = new_g_score
                open_set.add(neighbor)

    return -1


def get_neighbors(_walls, node):
    i, j = node
    neighbors = []

    for d in DIRECTION:
        ni, nj = i + d[0], j + d[1]

        if ni >= 0 and nj >= 0 and ni <= GRID_LEN and nj <= GRID_LEN:
            if (ni, nj) not in _walls:
                neighbors.append((ni, nj))

    return neighbors


def part1():
    # we dont need heuristic since we are at one end of grid. Heuristic would only add more
    # cycles and not provide much benefit. So in a way I am using Dijkstra or BFS since cost
    # is distributed equally
    bytes_to_check = set(total_bytes[:1024])
    num_steps = a_star_search(bytes_to_check, (0, 0), (GRID_LEN, GRID_LEN))
    return num_steps


def part2():
    # use binary search to speed it up
    L = 0
    R = len(total_bytes)
    num_byte = -1

    while True:
        num_byte = (L + R) // 2
        num_steps = a_star_search(
            set(total_bytes[:num_byte]), (0, 0), (GRID_LEN, GRID_LEN)
        )
        if num_steps == -1:
            R = num_byte
        else:
            L = num_byte

        if L == R or (R - L == 1):
            break

    _byte = total_bytes[num_byte]
    return f"{_byte[0]},{_byte[1]}"


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 278
assert ans_part_2 == "43,12"
