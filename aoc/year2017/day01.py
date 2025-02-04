from aoc.utils import read_input

ms = list(read_input(2017, 1).rstrip())
nl = len(ms)


def run(check_len):
    ms.extend(ms[:check_len])

    digits = []
    for i in range(0, len(ms)):
        if ms[i] == ms[i + check_len]:
            digits.append(int(ms[i]))

    return sum(digits)


print("Part1 solution: ", run(1))
print("Part2 solution:", run(len(ms) // 2))
