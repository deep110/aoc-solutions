from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

p = re.compile(r"Step ([A-Z]) must be finished before step ([A-Z]) can begin.")

def t(x):
    _s = p.search(x)
    return ord(_s.group(1)), ord(_s.group(2))

a = list(map(lambda x: t(x), ms))
ans = []
start = 66

for i in a:
    pass

def part1():
    pass

def part2():
    pass

print("Part1 solution: ", part1())
print("Part2 solution: ", part2())
