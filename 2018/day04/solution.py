from collections import defaultdict
from datetime import datetime
from os import path
import re


with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

PATTERN = re.compile(r"\[(.*)\] (.*)")


def extract_time(x):
    _q = PATTERN.search(x)
    return datetime.strptime(_q.group(1), "%Y-%m-%d %H:%M"), _q.group(2)


def setup():
    q = re.compile(r"Guard #(.*) begins shift")
    a = list(map(lambda x: extract_time(x), ms))
    a.sort(key=lambda r: r[0])
    sleep_mappings = defaultdict(lambda: [0] * 60)

    ongoing_guard = None
    sleep_st = None
    for dt, msg in a:
        _m = q.search(msg)
        if _m:
            ongoing_guard = int(_m.group(1))

        if "falls asleep" in msg:
            sleep_st = dt.minute

        elif "wakes up" in msg:
            guard_mapping = sleep_mappings[ongoing_guard]
            for m in range(sleep_st, dt.minute):
                guard_mapping[m] += 1

    return sleep_mappings


def part1(_mappings):
    guard_id = None
    max_time = -1
    for gid in _mappings:
        total_slp_time = sum(_mappings[gid])
        if total_slp_time > max_time:
            max_time = total_slp_time
            guard_id = gid

    max_slp = _mappings[guard_id].index(max(_mappings[guard_id]))
    return guard_id * max_slp


def part2(_mappings):
    guard_id = None
    max_time = -1
    for gid in _mappings:
        total_slp_time = max(_mappings[gid])
        if total_slp_time > max_time:
            max_time = total_slp_time
            guard_id = gid

    max_slp = _mappings[guard_id].index(max(_mappings[guard_id]))
    return guard_id * max_slp


sl_mappings = setup()

ans_part_1 = part1(sl_mappings)
ans_part_2 = part2(sl_mappings)

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 84834
assert ans_part_2 == 53427
