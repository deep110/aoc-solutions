from collections import defaultdict
import re
from aoc.utils import read_input

PATTERN = re.compile(r"Step ([A-Z]) must be finished before step ([A-Z]) can begin.")

ms = read_input(2018, 7).split("\n")
steps = list(map(lambda x: tuple(PATTERN.search(x).groups()), ms))


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.incoming_edges = defaultdict(list)

    def add_node(self, from_node, to_node):
        self.graph[from_node].append(to_node)
        self.incoming_edges[to_node].append(from_node)

    def get_outgoing_nodes(self, node):
        return self.graph[node]

    def get_incoming_edges(self, node):
        return self.incoming_edges[node]

    def nodes(self):
        return self.graph.keys()


def build_graph(_steps):
    _graph = Graph()
    for step in _steps:
        _graph.add_node(step[0], step[1])

    return _graph


def part1():
    step_order = []
    for g in graph.nodes():
        if len(graph.get_incoming_edges(g)) == 0:
            step_order.append(g)

    to_check_nodes = []
    while True:
        next_valid = graph.get_outgoing_nodes(step_order[-1])
        to_check_nodes.extend(next_valid)
        if len(to_check_nodes) == 0:
            break

        to_check_nodes = list(set(to_check_nodes))
        to_check_nodes.sort()

        while len(to_check_nodes) > 0:
            n = to_check_nodes.pop(0)
            if set(graph.get_incoming_edges(n)).issubset(set(step_order)):
                # prev tasks are done, pick it
                step_order.append(n)
                break
            else:
                to_check_nodes.append(n)

    return "".join(step_order)


def part2():
    pass


graph = build_graph(steps)

ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == "BGJCNLQUYIFMOEZTADKSPVXRHW"
# assert ans_part_2 == 39930
