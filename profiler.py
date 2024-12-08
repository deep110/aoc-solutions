import os
from time import time
from sys import argv
import subprocess


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

    print("| Day | Runtime | Status |")
    print("|-----|---------|--------|")

    # run for all days
    for day in range(1, 26):
        if os.path.isfile(f"{year}/day{day:02}/solution.py"):
            t1 = time()
            result = subprocess.run(
                ["python", f"{year}/day{day:02}/solution.py"],
                capture_output=True,
            )
            t2 = time()
            runtime = t2 - t1
            status = "✅" if result.returncode == 0 else "❌"

            print(f"| {day:02d} | {runtime:.4f}s | {status} |")

elif len(argv) == 3:
    year = to_int(1, "YEAR")
    day = to_int(2, "DAY")

    t1 = time()
    result = subprocess.call(["python", f"{year}/day{day:02}/solution.py"])
    t2 = time()
    print(f"Time taken: {(t2-t1):.4f}s")
else:
    print_usage()
