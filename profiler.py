import os
from sys import argv
import subprocess
from time import time


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
    year = to_int(1, "YEAR")

    # run for all days
    for day in range(1, 26):
        if os.path.isfile(f"{year}/day{day:02}/solution.py"):
            print(f"Day {day:02}")
            t1 = time()
            result = subprocess.call(["python", f"{year}/day{day:02}/solution.py"])
            t2 = time()
            print(f"Time taken: {(t2-t1):.4f}s")
            print("-------------")

elif len(argv) == 3:
    year = to_int(1, "YEAR")
    day = to_int(2, "DAY")

    t1 = time()
    result = subprocess.call(["python", f"{year}/day{day:02}/solution.py"])
    t2 = time()
    print(f"Time taken: {(t2-t1):.4f}s")
else:
    print_usage()
