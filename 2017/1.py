with open("input/input_1.txt") as f:
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


print("part1", run(1))
print("part2", run(int(nl/2)))
