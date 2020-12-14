import os
import shutil
from datetime import datetime
from sys import argv

SOLUTION_TEMPLATE = """from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

def part1():
    pass

def part2():
    pass

print("Part1 solution: ", part1())
print("Part2 solution: ", part2())
"""

def print_usage():
    print("Usage:", argv[0], "YEAR DAY")
    exit(1)

def to_int(i, name):
    try:
        return int(argv[i])
    except ValueError:
        print("Error:", name, "is not a number")
        print_usage()


if len(argv) == 2:
    day = to_int(1, "DAY")
    now = datetime.now()
    year = now.year
    if now.month < 12:
        year -= 1
elif len(argv) == 3:
    year = to_int(1, "YEAR")
    day = to_int(2, "DAY")
else:
    print_usage()

# create folder for particular day & year
dir_name = "{}/day{:02}".format(year, day)
os.makedirs(dir_name, exist_ok=True)
with open(dir_name + "/solution.py", "w") as f:
    f.write(SOLUTION_TEMPLATE)
