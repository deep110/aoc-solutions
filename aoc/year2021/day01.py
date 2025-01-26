from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

ms = list(map(lambda x: int(x.strip()), ms))

def part1():
    num_inc = 0
    for i in range(1, len(ms)):
        if ms[i] > ms[i-1]:
            num_inc += 1

    return num_inc

def part2():
    num_inc = 0
    prev_sum = -1
    for i in range(2, len(ms)):
        new_sum = ms[i] + ms[i-1] + ms[i-2]
        if new_sum > prev_sum and prev_sum != -1:
            num_inc += 1
        prev_sum = new_sum

    return num_inc

print("Part1 solution: ", part1())
print("Part2 solution: ", part2())
