from os import path
import re
from typing import List

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()


class Program:
    def __init__(self, mask: str):
        self.mask = mask
        self.mems = {}

    def calculate_1_0_masks(self):
        len_mask = len(self.mask)
        mask_1 = ["0"] * len_mask
        mask_0 = ["0"] * len_mask

        for i in range(len_mask):
            if self.mask[i] == "1":
                mask_1[i] = "1"
            elif self.mask[i] == "0":
                mask_0[i] = "1"

        return (int("".join(mask_0), 2), int("".join(mask_1), 2))


def parse_programs():
    MASK_PATTERN = re.compile(r"mask = (.*)")
    MEM_PATTERN = re.compile(r"mem\[(\d+)\] = (\d+)")

    programs = []
    program = None
    for m in ms:
        if m.startswith("mask"):
            program = Program(MASK_PATTERN.match(m).group(1))
            programs.append(program)
        else:
            matched = MEM_PATTERN.match(m)
            program.mems[int(matched.group(1))] = int(matched.group(2))

    return programs


def part1(programs: List[Program]):
    global_mem = {}

    # we will go reverse, if memory is written, we skip it
    for i in range(len(programs) - 1, -1, -1):
        program = programs[i]
        mask_0, mask_1 = program.calculate_1_0_masks()

        for location, value in program.mems.items():
            if location in global_mem:
                continue

            # apply mask
            global_mem[location] = (value | mask_1) & ~mask_0

    return sum(global_mem.values())


def part2(programs: List[Program]):
    global_mem = {}

    # we will go reverse, if memory is written, we skip it
    for i in range(len(programs)):
        mask = programs[i].mask

        for location, value in programs[i].mems.items():
            result = list("{:036b}".format(location))
            x_locs = []

            for i in range(36):
                if mask[i] == "1":
                    result[i] = "1"
                elif mask[i] == "X":
                    x_locs.append(i)

            # Idea is this, We are taking an integer i and filling its binary bits into locations we want
            for i in range(2 ** len(x_locs)):
                bin_i = bin(i)[2:].zfill(len(x_locs))
                for j, loc in enumerate(x_locs):
                    result[loc] = bin_i[j]

                mem_loc = int("".join(result), 2)
                global_mem[mem_loc] = value

    return sum(global_mem.values())


PROGRAMS = parse_programs()

ans_part_1 = part1(PROGRAMS)
ans_part_2 = part2(PROGRAMS)

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 7477696999511
assert ans_part_2 == 3687727854171
