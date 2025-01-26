from aoc.utils import read_input
from aoc.year2019.intcode_computer import IntCodeComputer

instructions = [int(i) for i in read_input(2019, 9).split(",")]


def run(input):
    comp = IntCodeComputer(instructions[:], input, extra_memory=150)
    while not comp.is_halted:
        comp.run_program()
    return comp.outputs[-1]


ans_part_1 = run(1)
ans_part_2 = run(2)

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 2204990589
assert ans_part_2 == 50008
