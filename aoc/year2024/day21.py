from aoc.utils import read_input


NUM_KEYPAD = [["7", "8", "9"], ["4", "5", "6"], ["", "0", "A"]]
DIR_KEYPAD = [["", "^", "A"], ["<", "v", ">"]]

ms = read_input(2024, 21).split("\n")


def find_next_num_seq():
    pass


def part1():
    print(ms)


def part2():
    pass


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 0
assert ans_part_2 == 0
