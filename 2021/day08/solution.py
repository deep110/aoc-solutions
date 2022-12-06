from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

def part1():
    outputs = list(map(lambda x: x.strip().split("|")[1].strip().split(" "), ms))
    num_times = 0
    for out in outputs:
        num_times += sum(map(lambda x : len(x) < 5 or len(x) == 7, out))

    return num_times


def part2():
    pass

print("Part1 solution: ", part1())
print("Part2 solution: ", part2())
