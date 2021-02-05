from os import path
import re
from datetime import datetime as dt
import numpy as np


with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

a = list(map(lambda x: x.rstrip("\n"), ms))
p = re.compile(r"\[(.*)\] (.*)")

def t(x):
    _q = p.search(x)
    if _q:
        return dt.strptime(_q.group(1), '%Y-%m-%d %H:%M'), _q.group(2)


a = list(map(lambda x: t(x), a))
a.sort(key=lambda r: r[0])


def setup():
    q = re.compile(r'Guard #(.*) begins shift')
    h = {}
    ongoing_guard = None
    asp = None
    for i in a:
        _m = q.search(i[1])
        if _m:
            ongoing_guard = int(_m.group(1))

        if 'falls asleep' in i[1]:
            r = h.get(ongoing_guard, np.zeros(60))
            asp = i[0].minute
            h[ongoing_guard] = r

        if 'wakes up' in i[1]:
            h[ongoing_guard][asp:i[0].minute] += 1

    return h

def part1(_mappings):
    k = []
    for i in _mappings:
        k.append(np.sum(_mappings[i]))

    guard_id = list(_mappings.keys())[int(np.argmax(np.asarray(k)))]
    return guard_id * np.argmax(_mappings[guard_id])


def part2(_mappings):
    k = []
    for i in _mappings:
        k.append(np.max(_mappings[i]))

    guard_id = list(_mappings.keys())[int(np.argmax(np.asarray(k)))]
    return guard_id * np.argmax(_mappings[guard_id])


mappings = setup()

print("Part1 solution: ", part1(mappings))
print("Part2 solution: ", part2(mappings))
