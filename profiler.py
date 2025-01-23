import os
import importlib.util
import sys
import time
from sys import argv
import io
from contextlib import redirect_stdout
import traceback
from typing import Optional, Tuple

import plotext as plt


def print_usage():
    print("Usage:", argv[0], "YEAR DAY")
    exit(1)


def to_int(i, name):
    try:
        return int(argv[i])
    except ValueError:
        print("Error:", name, "is not a number")
        print_usage()


def load_solution_module(
    year: int, day: int, suppress_output: bool = True
) -> Optional[Tuple[float, bool, str]]:
    """
    Load and run a solution module for a specific day, measuring its runtime.

    Returns:
    Tuple of (runtime in ms, success boolean, error message if any)
    """
    solution_file = f"{year}/day{day:02}/solution.py"

    if not os.path.isfile(solution_file):
        return None

    try:
        # Get the absolute path and setup the spec
        abs_path = os.path.abspath(solution_file)
        module_name = f"solution_y{year}_d{day}"
        spec = importlib.util.spec_from_file_location(module_name, abs_path)

        if spec is None or spec.loader is None:
            return 0, False, f"Failed to create module spec for day {day}"

        # Create the module and execute it
        module = importlib.util.module_from_spec(spec)

        # Change to the solution directory
        original_dir = os.getcwd()
        os.chdir(os.path.dirname(abs_path))

        # Time the execution
        start = time.perf_counter()
        try:
            if suppress_output:
                # Redirect stdout to devnull when suppressing output
                with redirect_stdout(io.StringIO()):
                    spec.loader.exec_module(module)
            else:
                spec.loader.exec_module(module)
            success = True
            error_msg = ""
        except Exception:
            success = False
            # Get the full traceback information
            exc_type, exc_value, exc_tb = sys.exc_info()
            error_msg = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
        finally:
            end = time.perf_counter()
            runtime_ms = (end - start) * 1000

        os.chdir(original_dir)

        return runtime_ms, success, error_msg

    except Exception:
        # Get the full traceback information
        exc_type, exc_value, exc_tb = sys.exc_info()
        tb_str = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
        return 0, False, tb_str


if len(argv) == 2:
    year = to_int(1, "YEAR")
    total_time = 0

    x_problems = []
    y_runtimes = []

    print("| Day | Runtime | Status |")
    print("|----|--------|----|")

    # run for all days
    for day in range(1, 26):
        result = load_solution_module(year, day)
        if result is None:
            continue

        runtime, success, error = result
        status = "✅" if success else "❌"
        total_time += runtime

        x_problems.append(f"{day:02d}")
        y_runtimes.append(runtime)

        print(f"| {day:02d} | {runtime:.2f}ms | {status} |")

    print("|----|--------|----|")

    print(f"Time taken in {year}: ", total_time, "ms")

    plt.bar(x_problems, y_runtimes, width=0.5, label="Run Time (ms)", color=200)
    plt.plot_size(height=plt.terminal_height() * 0.6)
    plt.theme("clear")
    plt.title("AOC 2024")
    plt.xlabel("Day")
    plt.show()

elif len(argv) == 3:
    year = to_int(1, "YEAR")
    day = to_int(2, "DAY")

    result = load_solution_module(year, day, suppress_output=False)
    if result is None:
        print("No solution found")
    else:
        runtime, success, error = result
        print(f"Time taken: {runtime}ms")
        if error:
            print(error)
else:
    print_usage()
