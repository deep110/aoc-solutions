from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    arr = list(map(lambda x: int(x), f.read().split(",")))


def run_program(cs, noun, verb):
    cs[1] = noun
    cs[2] = verb
    for i in range(0, len(cs), 4):
        if cs[i] == 99:
            break
        if cs[i] == 1:
            cs[cs[i + 3]] = cs[cs[i + 1]] + cs[cs[i + 2]]
        if cs[i] == 2:
            cs[cs[i + 3]] = cs[cs[i + 1]] * cs[cs[i + 2]]

    return cs[0]


def part1():
    b = arr[:]
    return run_program(b, 12, 2)


def part2():
    final_out = 19690720

    # for noun, starting from back is better
    for noun in range(99, -1, -1):
        for verb in range(1, 100):
            b = arr[:]
            if run_program(b, noun, verb) == final_out:
                return noun * 100 + verb


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 4090689
assert ans_part_2 == 7733
