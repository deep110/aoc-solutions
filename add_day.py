import os
from datetime import datetime
from sys import argv

SOLUTION_TEMPLATE = """from aoc.utils import read_input

ms = read_input({}, {})


def part1():
    pass

    
def part2():
    pass


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 0
assert ans_part_2 == 0
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
dir_name = "aoc/year{}".format(year)
os.makedirs(dir_name, exist_ok=True)

if not os.path.exists(dir_name + "/day{:02}.py".format(day)):
    with open(f"{dir_name}/day{day:02}.py", "w") as f:
        f.write(SOLUTION_TEMPLATE.format(year, day))

    with open(f"input/{year}/day{day:02}.txt", "w") as f:
        f.write("")
