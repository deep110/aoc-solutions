from itertools import permutations
from os import path
from typing import List
import sys

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from intcode_computer import IntCodeComputer

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    instructions = list(map(lambda x: int(x), f.read().split(",")))


def part1():
    thrusts = []
    for phases in permutations([0, 1, 2, 3, 4]):
        amp_out = 0
        for i in phases:
            computer = IntCodeComputer(instructions[:], i)
            amp_out = computer.run_program(amp_out)

        thrusts.append(amp_out)

    return max(thrusts)


def part2():
    thrusts = []
    for phases in permutations([9, 8, 7, 6, 5]):
        computers: List[IntCodeComputer] = []
        for i in range(5):
            computers.append(IntCodeComputer(instructions[:], phases[i]))

        idx = 0
        amp_out = 0
        while True:
            amp_out = computers[idx].run_program(amp_out)
            if idx == 4 and computers[idx].is_halted:
                break

            idx = (idx + 1) % 5
        thrusts.append(amp_out)

    return max(thrusts)


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 255840
assert ans_part_2 == 84088865
