from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.read().strip()


ms = list(ms)
nl = len(ms)

def run(check_len):
    ms.extend(ms[:check_len])

    digits = []
    for i in range(0, nl):
        if ms[i] == ms[i+check_len]:
            digits.append(int(ms[i]))

    return sum(digits)


print("Part1 solution: ", run(1))
print("Part2 solution:", run(int(nl/2)))
