from collections import defaultdict
from itertools import combinations
from typing import Dict, Set
from aoc.utils import read_input

ms = read_input(2024, 23).split("\n")

computers = list(map(lambda x: x.split("-"), ms))
connections = defaultdict(set)
for comp in computers:
    connections[comp[0]].add(comp[1])
    connections[comp[1]].add(comp[0])


def part1():
    sets_of_3 = set()
    for comp in connections:
        if comp[0] == "t":
            for comp_a, comp_b in combinations(connections[comp], 2):
                if comp_b in connections[comp_a]:
                    _set = [comp, comp_a, comp_b]
                    _set.sort()
                    sets_of_3.add(tuple(_set))

    return len(sets_of_3)


def bron_kerbosch_largest_clique(
    graph: Dict[str, Set[str]],
    clique: Set[str],
    candidates: Set[str],
    processed: Set[str],
) -> Set[str]:
    """
    Implementation of the Bron-Kerbosch algorithm with pivot for finding only largest
    cliques in an undirected graph.

    Parameters:
    -----------
    graph : Dict[str, Set[str]]
        The graph represented as an adjacency list where each key is a vertex (string)
        and its value is a set of vertices it's connected to
    clique : Set[str]
        The current clique being built
    candidates : Set[str]
        Set of vertices that can be added to the clique (prospective vertices)
    processed : Set[str]
        Set of vertices that have been processed (excluded vertices)

    Returns:
    --------
    Set[str]
        List of all maximal cliques found in the graph
    """

    # If both P and X are empty, we've found a maximal clique
    if not candidates and not processed:
        return clique

    # start with whatever clique we have, which is empty by default
    max_clique = clique

    # Choose a pivot vertex to optimize the algorithm
    # We choose from P union X to maximize the number of vertices we can skip
    pivot = max((len(graph[v]), v) for v in candidates.union(processed))[1]

    # Calculate vertices we can skip based on the pivot
    skip_vertices = graph[pivot] if pivot else set()

    # Process each vertex that could extend the current clique
    for v in candidates - skip_vertices:
        neighbors = graph[v]

        # Recursively find cliques with:
        # - r ∪ {v}: Add current vertex to the clique
        # - p ∩ N(v): Only consider vertices that are connected to v
        # - x ∩ N(v): Only consider excluded vertices that are connected to v
        new_clique = bron_kerbosch_largest_clique(
            graph,
            clique.union({v}),
            candidates.intersection(neighbors),
            processed.intersection(neighbors),
        )

        if len(new_clique) > len(max_clique):
            max_clique = new_clique

        # Move vertex v from candidates to processed
        candidates.remove(v)
        processed.add(v)

    return max_clique


# we will use Bron-Kerbosch algorithm to find largest clique, which is our solution
def part2():
    largest_clique = bron_kerbosch_largest_clique(
        connections,
        clique=set(),
        candidates=set(connections.keys()),
        processed=set(),
    )
    largest_clique = list(largest_clique)
    largest_clique.sort()

    return ",".join(largest_clique)


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 1110
assert ans_part_2 == "ej,hm,ks,ms,ns,rb,rq,sc,so,un,vb,vd,wd"
