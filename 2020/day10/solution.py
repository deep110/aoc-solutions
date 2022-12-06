from os import path

with open(path.join(path.dirname(__file__), "test.txt")) as f:
    ms = f.readlines()

ms = list(map(lambda x: int(x), ms))

def part1():
    no_threes = 1
    no_one = 0
    ms.sort()
    ms.insert(0, 0)
    for i in range(1, len(ms)):
        diff = ms[i] - ms[i-1]
        if diff == 1:
            no_one += 1
        elif diff == 3:
            no_threes += 1

    return no_one * no_threes

def part2():
    ms.sort()
    ms.insert(0, 0)
    diffs = []
    for i in range(1, len(ms)):
        diff = ms[i] - ms[i-1]
        diffs.append(diff)

    print(diffs)
    series_of_ones = []
    is_active = False
    is_one_skipped = False
    for i in range(len(diffs)-1, -1, -1):
        if i == 3:
            is_active = False
            is_one_skipped = False
        else:
            if is_active:
                

# print("Part1 solution: ", part1())
print("Part2 solution: ", part2())
