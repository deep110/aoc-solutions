from itertools import permutations
from os import path
from typing import List

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    instructions = list(map(lambda x: int(x), f.read().split(",")))


class IntCodeComputer:
    def __init__(self, instructions, input: int):
        self.codes = instructions
        self.is_halted = False
        self.ip = 0  # instruction_pointer
        self.outputs = []
        self.inputs = [input]
        self.input_counter = 0

    def get_value(self, j, mode):
        if mode == 1:
            return self.codes[j]
        else:
            return self.codes[self.codes[j]]

    def set_value(self, j, value, mode):
        if mode == 1:
            self.codes[j] = value
        else:
            self.codes[self.codes[j]] = value

    def run_program(self, more_input):
        if self.is_halted:
            return self.outputs[-1]

        self.inputs.append(more_input)

        while True:
            x = self.codes[self.ip]
            op_code, mode1, mode2, mode3 = (
                x % 100,
                (x // 100) % 10,
                (x // 1000) % 10,
                x // 10000,
            )

            if op_code == 99:
                self.is_halted = True
                break
            elif op_code == 1:
                val = self.get_value(self.ip + 1, mode1) + self.get_value(
                    self.ip + 2, mode2
                )
                self.set_value(self.ip + 3, val, mode3)
                self.ip += 4
            elif op_code == 2:
                val = self.get_value(self.ip + 1, mode1) * self.get_value(
                    self.ip + 2, mode2
                )
                self.set_value(self.ip + 3, val, mode3)
                self.ip += 4
            elif op_code == 3:
                self.set_value(self.ip + 1, self.inputs[self.input_counter], mode1)
                self.input_counter += 1
                self.ip += 2
            elif op_code == 4:
                self.outputs.append(self.get_value(self.ip + 1, mode1))
                self.ip += 2
                break
            elif op_code == 5:
                if self.get_value(self.ip + 1, mode1) != 0:
                    self.ip = self.get_value(self.ip + 2, mode2)
                else:
                    self.ip += 3
            elif op_code == 6:
                if self.get_value(self.ip + 1, mode1) == 0:
                    self.ip = self.get_value(self.ip + 2, mode2)
                else:
                    self.ip += 3
            elif op_code == 7:
                val = self.get_value(self.ip + 1, mode1) < self.get_value(
                    self.ip + 2, mode2
                )
                self.set_value(self.ip + 3, int(val), mode3)
                self.ip += 4
            elif op_code == 8:
                val = self.get_value(self.ip + 1, mode1) == self.get_value(
                    self.ip + 2, mode2
                )
                self.set_value(self.ip + 3, int(val), mode3)
                self.ip += 4

        return self.outputs[-1]


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
