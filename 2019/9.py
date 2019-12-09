with open("input/input_9.txt") as f:
    cs = f.read().strip().split(",")

cs = list(map(lambda x: int(x), cs))

def run_program(cs, _input, relative_base):
    def handle_param_out(x: int):
        z = str(x).zfill(5)
        
        return (int(z[3:]), int(z[2]), int(z[1]), int(z[0]))

    def get_value(j, codes, mode, _rb):
        if mode == 1:
            return codes[j]
        elif mode == 0:
            return codes[codes[j]]
        else:
            return codes[codes[j] + _rb]

    def set_value(j, value, codes, mode, _rb):
        if mode == 1:
            codes[j] = value
        elif mode == 0:
            codes[codes[j]] = value
        else:
            codes[codes[j] + _rb] = value

    cs.extend([0] * 500)
    i = 0
    outputs = []
    rb = relative_base

    while True:
        po = handle_param_out(cs[i])

        if po[0] == 99:
            break
        if po[0] == 1:
            val = get_value(i+1, cs, po[1], rb) + get_value(i+2, cs, po[2], rb)
            set_value(i+3, val, cs, po[3], rb)
            i += 4
        if po[0] == 2:
            val = get_value(i+1, cs, po[1], rb) * get_value(i+2, cs, po[2], rb)
            set_value(i+3, val, cs, po[3], rb)
            i += 4
        if po[0] == 3:
            set_value(i+1, _input, cs, po[1], rb)
            i += 2
        if po[0] == 4:
            outputs.append(get_value(i+1, cs, po[1], rb))
            i += 2
        if po[0] == 5:
            fp = get_value(i+1, cs, po[1], rb)
            if fp != 0:
                i = get_value(i+2, cs, po[2], rb)
            else:
                i += 3
        if po[0] == 6:
            fp = get_value(i+1, cs, po[1], rb)
            if fp == 0:
                i = get_value(i+2, cs, po[2], rb)
            else:
                i += 3
        if po[0] == 7:
            val = get_value(i+1, cs, po[1], rb) < get_value(i+2, cs, po[2], rb)
            set_value(i+3, int(val), cs, po[3], rb)
            i += 4
        if po[0] == 8:
            val = get_value(i+1, cs, po[1], rb) == get_value(i+2, cs, po[2], rb)
            set_value(i+3, int(val), cs, po[3], rb)
            i += 4
        if po[0] == 9:
            rb = rb + get_value(i+1, cs, po[1], rb)
            i += 2

    return outputs[-1]

print("part1", run_program(cs[:], 1, 0))
print("part2", run_program(cs[:], 2, 0))
