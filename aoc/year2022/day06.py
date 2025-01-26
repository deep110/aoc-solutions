from aoc.utils import read_input

ms = read_input(2022, 6).split("\n")
buffer = ms[0]


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
