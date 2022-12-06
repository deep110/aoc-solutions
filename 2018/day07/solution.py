from os import path
import re

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

p = re.compile(r"Step ([A-Z]) must be finished before step ([A-Z]) can begin.")

def t(x):
    _s = p.search(x)
    return [_s.group(1), _s.group(2)]

events = list(map(lambda x: t(x), ms))
print(len(events), events[0], ms[0])

tasks = []
for e in events:
    tasks.extend(e)
tasks = list(set(tasks))
tasks.sort()
print(tasks)

def part1():
    p = tasks
    for e in events:
        print("-"*30)
        print(e)
        print("Before: ", p)
        i, j = p.index(e[0]), p.index(e[1])
        if i < j:
            continue
        
        len_tasks = len(p)
        p = [*p[0:j], p[i], *p[j:i], *p[i+1:len_tasks]]
        print("After: ", p)


    return "".join(p)

def part2():
    pass

print("Part1 solution: ", part1())
print("Part2 solution: ", part2())
