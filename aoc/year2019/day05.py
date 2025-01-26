"""
# Sunny with a Chance of Asteroids
"""

from aoc.utils import read_input
from aoc.year2019.intcode_computer import IntCodeComputer

instructions = [int(i) for i in read_input(2019, 5).split(",")]


def run_program(input):
    comp = IntCodeComputer(instructions.copy(), input)
    while not comp.is_halted:
        comp.run_program()
    return comp.outputs[-1]


ans_part_1 = run_program(1)
ans_part_2 = run_program(5)

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 16574641
assert ans_part_2 == 15163975
