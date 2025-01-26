import collections
from aoc.utils import read_input

ms = read_input(2022, 12).split("\n")

NUM_ROWS = len(ms)
NUM_COLUMNS = len(ms[0])


def parse_to_graph():
    graph = []
    start_coord = None
    end_coord = None

    for i in range(NUM_ROWS):
        graph.append([])
        for j in range(NUM_COLUMNS):
            if ms[i][j] == "S":
                start_coord = (i, j)
                graph[-1].append(0)
            elif ms[i][j] == "E":
                end_coord = (i, j)
                graph[-1].append(ord("z") - 97)
            else:
                graph[-1].append(ord(ms[i][j]) - 97)

    return graph, start_coord, end_coord


def is_in_grid(row, col):
    return (row >= 0) and (row < NUM_ROWS) and (col >= 0) and (col < NUM_COLUMNS)


def get_neighbors(c, graph, end):
    r_move = [-1, 0, 0, 1]
    c_move = [0, -1, 1, 0]
    ns = []

    for i in range(4):
        row = c[0] + r_move[i]
        col = c[1] + c_move[i]

        if is_in_grid(row, col) and graph[row][col] - graph[c[0]][c[1]] <= 1:
            ns.append((row, col))

    return ns


def bfs(graph, start_coord, end_coord):
    visited = set()
    queue = collections.deque()
    queue.append((start_coord, 1))

    while len(queue) > 0:
        vertex, path_len = queue.popleft()
        visited.add(vertex)

        for n in get_neighbors(vertex, graph, end_coord):
            if n == end_coord:
                return path_len
            elif n not in visited:
                visited.add(n)
                queue.append((n, path_len + 1))


def part1():
    graph, start_coord, end_coord = parse_to_graph()

    return bfs(graph, start_coord, end_coord)


def part2():
    min_distance = 1000
    graph, _, end_coord = parse_to_graph()

    for i in range(NUM_ROWS):
        for j in range(NUM_COLUMNS):
            if graph[i][j] == 0:
                dis = bfs(graph, (i, j), end_coord)
                if dis is not None and dis < min_distance:
                    min_distance = dis

    return min_distance


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 361
assert ans_part_2 == 354
