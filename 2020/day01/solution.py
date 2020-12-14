from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

ms = list(map(lambda x: int(x.strip()), ms))
_ms_set = set(ms)
_sum = 2020

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

    return a * b * c

print("Part1 solution: ", part1())
print("Part2 solution: ", part2())
