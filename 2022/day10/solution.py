from os import path
import re

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

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

        mt  = COMMAND.search(ms[pc])
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
    for i in range(30):
        rows.append("")

    for c in range(num_cycles):
        cp = (c % 40)

        pixel = "."
        if cp >= X - 1 and cp <= X+1:
            pixel = "█"
        rows[int(c / 40)] += pixel

        mt  = COMMAND.search(ms[pc])
        if mt[1] == "noop":
            pc += 1
        else:
            if add_in_progress:
                X += int(mt[2])
                add_in_progress = False
                pc += 1
            else:
                add_in_progress = True
        
    for i in rows:
        if len(i) > 0:
            print(i)

print("Part1 solution: ", part1())
print("Part2 solution: ", part2())
