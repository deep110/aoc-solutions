import re
from aoc.utils import read_input, image_arr_to_str

ms = read_input(2022, 10).split("\n")

COMMAND = re.compile(r"(addx|noop) ?(.*)")


def part1():
    X = 1
    num_cycles = 220
    pc = 0
    add_in_progress = False
    total = 0

    for i in range(1, num_cycles + 1):
        if i in [20, 60, 100, 140, 180, 220]:
            total += i * X

        mt = COMMAND.search(ms[pc])
        if mt[1] == "noop":
            pc += 1
        else:
            if add_in_progress:
                X += int(mt[2])
                add_in_progress = False
                pc += 1
            else:
                add_in_progress = True
    return total


def part2():
    X = 1
    num_cycles = 240
    pc = 0
    add_in_progress = False
    rows = []
    for i in range(20):
        rows.append("")

    for c in range(num_cycles):
        cp = c % 40

        pixel = "."
        if cp >= X - 1 and cp <= X + 1:
            # pixel = "█"
            pixel = "#"
        rows[int(c / 40)] += pixel

        mt = COMMAND.search(ms[pc])
        if mt[1] == "noop":
            pc += 1
        else:
            if add_in_progress:
                X += int(mt[2])
                add_in_progress = False
                pc += 1
            else:
                add_in_progress = True

    prepared_array = list(filter(lambda x: len(x) > 0, rows))
    res = image_arr_to_str(prepared_array)

    return res


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 16880
assert ans_part_2 == "RKAZAJBR"
