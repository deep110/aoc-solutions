from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()


elves_calories = [[]]
for i in ms:
    if i == "\n":
        elves_calories.append([])
    else:
        elves_calories[-1].append(int(i))

total_cal = []
for i in elves_calories:
    total_cal.append(sum(i))

def part1():
    return max(total_cal)

def part2():
    total_cal_sorted = sorted(total_cal, reverse=True)
    return sum(total_cal_sorted[:3])

ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 66719
assert ans_part_2 == 198551
