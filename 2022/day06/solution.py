from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

buffer = ms[0].strip()


def detect_marker(num_char):
    for i in range(len(buffer)):
        if len(set(buffer[i : i + num_char])) == num_char:
            return i + num_char


def part1():
    return detect_marker(4)


def part2():
    return detect_marker(14)


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 1300
assert ans_part_2 == 3986
