from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    instructions = list(map(lambda x: int(x), f.read().split(",")))


def get_value(j, codes, is_pos):
    if is_pos == 1:
        return codes[j]
    else:
        return codes[codes[j]]


def set_value(j, value, codes, is_pos):
    if is_pos == 1:
        codes[j] = value
    else:
        codes[codes[j]] = value


def run_program(_input):
    i = 0  # instruction_pointer
    outputs = []
    cs = instructions.copy()

    while True:
        x = cs[i]
        op_code, mode1, mode2, mode3 = (
            x % 100,
            (x // 100) % 10,
            (x // 1000) % 10,
            x // 10000,
        )

        if op_code == 99:
            break
        elif op_code == 1:
            val = get_value(i + 1, cs, mode1) + get_value(i + 2, cs, mode2)
            set_value(i + 3, val, cs, mode3)
            i += 4
        elif op_code == 2:
            val = get_value(i + 1, cs, mode1) * get_value(i + 2, cs, mode2)
            set_value(i + 3, val, cs, mode3)
            i += 4
        elif op_code == 3:
            set_value(i + 1, _input, cs, mode1)
            i += 2
        elif op_code == 4:
            outputs.append(get_value(i + 1, cs, mode1))
            i += 2
        elif op_code == 5:
            if get_value(i + 1, cs, mode1) != 0:
                i = get_value(i + 2, cs, mode2)
            else:
                i += 3
        elif op_code == 6:
            if get_value(i + 1, cs, mode1) == 0:
                i = get_value(i + 2, cs, mode2)
            else:
                i += 3
        elif op_code == 7:
            val = get_value(i + 1, cs, mode1) < get_value(i + 2, cs, mode2)
            set_value(i + 3, int(val), cs, mode3)
            i += 4
        elif op_code == 8:
            val = get_value(i + 1, cs, mode1) == get_value(i + 2, cs, mode2)
            set_value(i + 3, int(val), cs, mode3)
            i += 4

    return outputs[-1]


ans_part_1 = run_program(1)
ans_part_2 = run_program(5)

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 16574641
assert ans_part_2 == 15163975
