from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

NUM_INSTRUCTIONS = len(ms)


def parse_instruction(ins):
    k = ins.strip().split(" ")
    return (k[0], int(k[1]))


instructions = list(map(parse_instruction, ms))


def run_program():
    index = 0
    acc = 0
    visited_indexes = set()
    is_loop = False
    while True:
        visited_indexes.add(index)
        ins, num = instructions[index]
        if ins == "nop":
            index += 1
        elif ins == "acc":
            acc += num
            index += 1
        elif ins == "jmp":
            index += num

        if index in visited_indexes:
            is_loop = True
            break
        if index >= NUM_INSTRUCTIONS:
            break
    return acc, is_loop


def part1():
    acc, _ = run_program()
    return acc


def part2():
    for i, (op, number) in enumerate(instructions):
        original_op = op
        if op == "nop":
            instructions[i] = ("jmp", number)
        elif op == "jmp":
            instructions[i] = ("nop", number)
        else:
            continue
        acc, is_loop = run_program()
        if not is_loop:
            return acc
        instructions[i] = (original_op, number)


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 2034
assert ans_part_2 == 672
