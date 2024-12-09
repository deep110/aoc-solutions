from os import path
import itertools

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

def to_num(_k):
    _k = _k.rstrip('\n')
    return int(_k[1:]) if _k[0] == '+' else (-1 * int(_k[1:]))

ms = list(map(lambda x: to_num(x), ms))

def part1():
    return sum(ms)

def part2():
    z = 0
    curr = {0}

    for i in itertools.cycle(ms):
        z += i

        if z in curr:
            return z
        else:
            curr.add(z)


print("Part1 solution: ", part1())
print("Part2 solution: ", part2())
