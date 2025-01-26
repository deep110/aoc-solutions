from collections import defaultdict
import re
from aoc.utils import read_input

GATE_PATTERN = re.compile(r"^(.*) (XOR|OR|AND) (.*) -> (.*)")


def parse_input():
    ms = read_input(2024, 24).split("\n")
    wires = {}
    gates = {}
    break_idx = ms.index("")
    for i in ms[:break_idx]:
        wire, val = i.split(": ")
        wires[wire] = int(val)

    for j in ms[break_idx + 1 :]:
        gs = GATE_PATTERN.match(j)
        gates[gs[4]] = (gs[1], gs[2], gs[3])

    return wires, gates


def solve_circuit(wires: dict, gates: dict):
    stack = list(gates.keys())
    while stack:
        to_be_solve_gate = stack[-1]
        if to_be_solve_gate in wires:
            stack.pop()
            continue

        # check if gate is solvable
        g1, op, g2 = gates[to_be_solve_gate]
        if g1 in wires and g2 in wires:
            if op == "AND":
                wires[to_be_solve_gate] = wires[g1] and wires[g2]
            elif op == "OR":
                wires[to_be_solve_gate] = wires[g1] or wires[g2]
            else:
                wires[to_be_solve_gate] = wires[g1] ^ wires[g2]

            stack.pop()
        else:
            if g1 not in wires:
                stack.append(g1)
            if g2 not in wires:
                stack.append(g2)


def get_rule_idx(_gates):
    ridx = defaultdict(list)
    for r in _gates:
        v1, op, v2 = _gates[r]
        ridx[v1].append([v2, op, r])
        ridx[v2].append([v1, op, r])
    return ridx


WIRES, GATES = parse_input()


def part1():
    # solve gates
    solve_circuit(WIRES, GATES)

    final_value = []
    for wire, value in sorted(WIRES.items(), key=lambda x: x[0], reverse=True):
        if wire.startswith("z"):
            final_value.append(str(value))

    return int("".join(final_value), 2)


def part2():
    # our setup is a 45 bit ripple adder.
    swapped_wires = []
    ridx = get_rule_idx(GATES)
    for i in range(1, 45):
        xi = f"x{i:02}"
        zi = f"z{i:02}"
        if not any(
            v[2] in GATES[zi]
            for v in ridx[xi]
            if v[1] == "XOR" and GATES[zi][1] == "XOR"
        ):
            # find xor1 = x1 XOR y1
            xor1 = next(v[2] for v in ridx[xi] if v[1] == "XOR")

            # if output is not ai XOR xor1, then output is wrong,
            # swap output with ai XOR (xi XOR yi)
            if GATES[zi][1] != "XOR":
                xor2 = next(v[2] for v in ridx[xor1] if v[1] == "XOR")
                swapped_wires += [zi, xor2]
            else:
                and1 = next(v[2] for v in ridx[f"x{i - 1:02}"] if v[1] == "AND")
                or1 = next(v[2] for v in ridx[and1] if v[1] == "OR")
                xor2 = next(v[0] for v in ridx[or1] if v[1] == "XOR")
                swapped_wires += [xor1, xor2]

    swapped_wires.sort()
    return ",".join(swapped_wires)


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 52956035802096
assert ans_part_2 == "hnv,hth,kfm,tqr,vmv,z07,z20,z28"
