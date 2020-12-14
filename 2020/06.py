with open("input/input_6.txt") as f:
    ms = f.read()

ms = ms.split("\n\n")

def part1():
    c = 0
    for i in ms:
        j = set(i.replace("\n", ""))
        c += len(j)

    return c

def part2():
    c = 0
    for i in ms:
        j = list(map(lambda x: set(x), i.strip().split("\n")))
        k = set.intersection(*j)
        c += len(k)

    return c

part2()
