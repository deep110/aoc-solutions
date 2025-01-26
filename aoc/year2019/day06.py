from typing import Dict
from aoc.utils import read_input

cs = read_input(2019, 6).split("\n")


class Node:
    def __init__(self, value):
        self.value = value
        self.path = 0
        self.links = []
        self.parent_node = None

    def set_path(self, path):
        self.path = path

    def __str__(self):
        return str(self.value)


def set_paths(root: Node, path_val):
    root.set_path(path_val)
    uv = path_val + 1
    for i in root.links:
        set_paths(i, uv)


def get_and_set(_dict, val):
    n = _dict.get(val)
    if not n:
        n = Node(val)
        _dict[val] = n
    return n


def create_tree():
    node_dict = {"COM": Node("COM")}

    for i in cs:
        q = i.split(")")
        n1 = get_and_set(node_dict, q[0])
        n2 = get_and_set(node_dict, q[1])

        n1.links.append(n2)
        n2.parent_node = n1

    set_paths(node_dict["COM"], 0)

    return node_dict


def part1(tree: Dict[str, Node]):
    total = 0
    for i in tree.values():
        total += i.path

    return total


def part2(tree: Dict[str, Node]):
    # we create path from "SAN" -> "COM", then
    # when creating a path from "YOU" -> "COM", first node we find will be the common node
    # for shortest path

    # create path between santa and COM
    path_santa = set()
    node_val = "SAN"
    while node_val != "COM":
        node_val = tree[node_val].parent_node.value
        path_santa.add(node_val)

    # find the node which is in path of SAN-COM path
    node_val = "YOU"
    while True:
        node_val = tree[node_val].parent_node.value
        if node_val in path_santa:
            break

    req_node = tree[node_val]
    return (tree["YOU"].path - req_node.path) + (tree["SAN"].path - req_node.path) - 2


TREE = create_tree()

ans_part_1 = part1(TREE)
ans_part_2 = part2(TREE)

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 271151
assert ans_part_2 == 388
