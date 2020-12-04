with open("input/input_1.txt") as f:
    ms = f.readlines()

ms = list(map(lambda x: int(x.strip()), ms))

_sum = 2020

_ms_set = set(ms)

def part1():
    a, b = (None, None)

    for i in ms:
        if (_sum - i) in _ms_set:
            a, b = (i, _sum - i)
            break

    return a*b

def part2():
    a, b, c = (None, None, None)

    for i in ms:
        for j in ms:
            k = _sum - i - j
            if k in _ms_set:
                a, b, c = (i, j, k)
                break

    return a*b * c

print(part2())