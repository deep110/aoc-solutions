from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

NUM_INSTRUCTIONS = len(ms)

def parse_instrcution(ins):
    k = ins.strip().split(" ")
    return (k[0], int(k[1]))


def run_program(instructions):
    index = 0
    acc = 0
    visited_indexes = []
    is_break = False
    while True:
        visited_indexes.append(index)
        ins, num = parse_instrcution(instructions[index])
        if ins == "nop":
            index += 1
        elif ins == "acc":
            acc += num
            index += 1
        elif ins == "jmp":
            index += num
        
        if index in visited_indexes:
            is_break = True
            break
        if index >= NUM_INSTRUCTIONS:
            break
    return acc, is_break

def part1():
    acc, _ = run_program(ms)
    return acc

def part2():
    for i, ins in enumerate(ms):
        k = ms[i]
        if "nop" in ins:
            ms[i] = ms[i].replace("nop", "jmp")
        elif "jmp" in ins:
            ms[i] = ms[i].replace("jmp", "nop")
        else:
            continue
        acc, is_break = run_program(ms)
        ms[i] = k
        if not is_break:
            return acc

    return None

print("Part1 solution: ", part1())
print("Part2 solution: ", part2())
