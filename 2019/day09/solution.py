from os import path
from typing import List

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    cs = list(map(lambda x: int(x), f.read().split(",")))


class IntCodeComputer:
    def __init__(
        self, instructions: List[int], input: int = None, relative_base: int = 0
    ):
        self.codes = instructions
        self.is_halted = False
        self.ip = 0  # instruction_pointer
        self.outputs = []
        self.inputs = [input] if input else []
        self.input_counter = 0
        self.rb = relative_base

        # extend memory
        self.codes.extend([0] * 200)

    def get_value(self, j, mode):
        if mode == 1:
            return self.codes[j]
        elif mode == 0:
            return self.codes[self.codes[j]]
        else:
            return self.codes[self.codes[j] + self.rb]

    def set_value(self, j, value, mode):
        if mode == 1:
            self.codes[j] = value
        elif mode == 0:
            self.codes[self.codes[j]] = value
        else:
            self.codes[self.codes[j] + self.rb] = value

    def run_program(self, more_input: int = None):
        if self.is_halted:
            return self.outputs[-1]

        if more_input:
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
            elif op_code == 9:
                self.rb = self.rb + self.get_value(self.ip + 1, mode1)
                self.ip += 2

        return self.outputs[-1]


def run(input):
    comp = IntCodeComputer(cs[:], input, 0)
    while not comp.is_halted:
        comp.run_program()
    return comp.outputs[-1]


ans_part_1 = run(1)
ans_part_2 = run(2)

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 2204990589
assert ans_part_2 == 50008
