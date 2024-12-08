from os import path

with open(path.join(path.dirname(__file__), "test.txt")) as f:
    ms = f.readlines()

rk_paths = []
bounds = []
for i in ms:
    rk_paths.append(list(map(lambda x: tuple(x.split(",")), i.strip().split(" -> "))))


def part1():
    print(rk_paths)


def part2():
    pass


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 5588
assert ans_part_2 == 23958
