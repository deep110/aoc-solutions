from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

reports = list(map(lambda x: x.split(), ms))


def is_safe(report):
    # all diffs should be positive or negative and between 1-3
    diffs = [int(report[i + 1]) - int(report[i]) for i in range(len(report) - 1)]
    is_in_range = all((1 <= abs(x) <= 3) for x in diffs)
    if not is_in_range:
        return False

    is_monotonic = all(x > 0 for x in diffs) or all(x < 0 for x in diffs)
    if is_monotonic:
        return True


def part1():
    return [is_safe(report) for report in reports].count(True)


def part2():
    safes = 0
    for report in reports:
        if is_safe(report):
            safes += 1
            continue
        for i in range(len(report)): 
           if is_safe(report[:i] + report[i+1:]):
               safes += 1
               break

    return safes


print("Part1 solution: ", part1())
print("Part2 solution: ", part2())
