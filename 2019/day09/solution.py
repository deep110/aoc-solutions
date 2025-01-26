from os import path
import sys

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from intcode_computer import IntCodeComputer

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    cs = list(map(lambda x: int(x), f.read().split(",")))


def run(input):
    comp = IntCodeComputer(cs[:], input, extra_memory=150)
    while not comp.is_halted:
        comp.run_program()
    return comp.outputs[-1]


ans_part_1 = run(1)
ans_part_2 = run(2)

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 2204990589
assert ans_part_2 == 50008
