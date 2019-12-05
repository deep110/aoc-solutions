with open("input/input_5.txt") as f:
    cs = f.read().strip().split(",")

cs = list(map(lambda x: int(x), cs))

def handle_param_out(x: int):
    if x < 9:
        return (x, 0, 0, 0)
    z = str(x).zfill(5)
    
    return (int(z[3:]), int(z[2]), int(z[1]), int(z[0]))


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
    arr_len = len(cs)
    i = 0
    outputs = []

    while i < arr_len:
        po = handle_param_out(cs[i])

        if po[0] == 99:
            break
        if po[0] == 1:
            val = get_value(i+1, cs, po[1]) + get_value(i+2, cs, po[2])
            set_value(i+3, val, cs, po[3])
            i += 4
        if po[0] == 2:
            val = get_value(i+1, cs, po[1]) * get_value(i+2, cs, po[2])
            set_value(i+3, val, cs, po[3])
            i += 4
        if po[0] == 3:
            cs[cs[i+1]] = _input
            i += 2
        if po[0] == 4:
            outputs.append(cs[cs[i+1]])
            i += 2
        if po[0] == 5:
            fp = get_value(i+1, cs, po[1])
            if fp != 0:
                i = get_value(i+2, cs, po[2])
            else:
                i += 3
        if po[0] == 6:
            fp = get_value(i+1, cs, po[1])
            if fp == 0:
                i = get_value(i+2, cs, po[2])
            else:
                i += 3
        if po[0] == 7:
            val = get_value(i+1, cs, po[1]) < get_value(i+2, cs, po[2])
            set_value(i+3, int(val), cs, po[3])
            i += 4
        if po[0] == 8:
            val = get_value(i+1, cs, po[1]) == get_value(i+2, cs, po[2])
            set_value(i+3, int(val), cs, po[3])
            i += 4

    return outputs


print("part1", run_program(1))
print("part2", run_program(5))