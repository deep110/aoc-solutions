from collections import defaultdict


program = [2, 4, 1, 1, 7, 5, 0, 3, 4, 3, 1, 6, 5, 5, 3, 0]


def run_program(regA, program):
    registers = [regA, 0, 0]
    instruction_pointer = 0
    output = []
    while instruction_pointer < len(program):
        op_code = program[instruction_pointer]
        lit_operand = program[instruction_pointer + 1]
        combo_operand = lit_operand if lit_operand < 4 else registers[lit_operand - 4]

        match op_code:
            case 0:
                registers[0] = registers[0] // (2**combo_operand)
            case 1:
                registers[1] = registers[1] ^ lit_operand
            case 2:
                registers[1] = combo_operand % 8
            case 3:
                if registers[0] != 0:
                    instruction_pointer = lit_operand
                    instruction_pointer -= 2
            case 4:
                registers[1] = registers[1] ^ registers[2]
            case 5:
                output.append(combo_operand % 8)
            case 6:
                registers[1] = registers[0] // (2**combo_operand)
            case 7:
                registers[2] = registers[0] // (2**combo_operand)

        instruction_pointer += 2
    return output


def part1():
    output = run_program(18427963, program)
    output_str = list(map(lambda x: str(x), output))

    return ",".join(output_str)


def part2():
    """
    Program does this:
    1. Take modulo 8 of A i.e last 3 digits
    2. do some operations with that
    3. Remove those last 3 digits.

    while True:
        regB = (regA % 8) ^ 1
        regC = regA // (2**regB)
        regB = regB ^ regC ^ 6
        regA = regA // 8

        output.append(regB % 8)
        if regA == 0:
            break
    """
    len_program = len(program)
    registerA = ["0"] * len_program  # octal values
    index = 0
    backtrack = defaultdict(list)

    while index < len_program:
        for i in range(8):
            registerA[index] = str(i)

            rA_int = int("".join(registerA), 8)
            output = run_program(rA_int, program)

            out_index = len_program - 1 - index
            if len(output) == len_program and output[out_index] == program[out_index]:
                backtrack[index].append(registerA[index])

        if len(backtrack[index]) > 0:
            registerA[index] = backtrack[index].pop(0)
            index += 1
        else:
            # backtrack
            while True:
                index -= 1
                if len(backtrack[index]) > 0:
                    registerA[index] = backtrack[index].pop(0)
                    index += 1
                    break

    return int("".join(registerA), 8)


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == "2,0,7,3,0,3,1,3,7"
assert ans_part_2 == 247839539763386
