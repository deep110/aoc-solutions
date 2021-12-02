from os import path
import re

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

REG = re.compile(r"(forward|up|down) (\d+)")

def part1():
    x = 0
    y = 0
    for i in ms:
        q = REG.search(i.strip())
        val = int(q[2])

        if q[1] == "up":
            y -= val
        elif q[1] == "down":
            y += val
        elif q[1] == "forward":
            x += val
        else:
            print(i)
    
    return x * y

def part2():
    x = 0
    y = 0
    aim = 0
    for i in ms:
        q = REG.search(i.strip())
        val = int(q[2])

        if q[1] == "up":
            aim -= val
        elif q[1] == "down":
            aim += val
        elif q[1] == "forward":
            x += val
            y += aim * val
        else:
            print(i)
    
    return x * y

print("Part1 solution: ", part1())
print("Part2 solution: ", part2())
