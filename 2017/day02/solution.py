from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

ms = list(map(lambda x: x.split("\t"), ms))
ims = []
for i in ms:
    ims.append(list(map(lambda x: int(x.strip()), i)))

def part1():
    checksums = []
    for i in ims:
        checksums.append(max(i) - min(i))

    return sum(checksums)

def part2():    
    def find_nos(row):
        for i in row:
            for j in row:
                if i != j and i % j == 0:
                    return int(i/j)
        return 0

    res = []
    for i in ims:
        a = find_nos(i)
        res.append(a)

    return sum(res)


print("Part1 solution: ", part1())
print("Part2 solution: ", part2())
