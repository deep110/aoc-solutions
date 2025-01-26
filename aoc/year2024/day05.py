from collections import defaultdict
from aoc.utils import read_input

ms = read_input(2024, 5).split("\n")


rules = defaultdict(list)
for r in ms[: ms.index("")]:
    p = r.split("|")
    rules[p[0]].append(p[1])


def part1():
    updates = list(map(lambda x: x.split(","), ms[ms.index("") + 1 :]))

    middle_pg_sum = 0
    invalid_updates = []
    for update in updates:
        valid = True
        len_up = len(update)
        for j in range(len_up - 1):
            for k in range(j + 1, len_up):
                if update[k] not in rules[update[j]]:
                    valid = False
                    break
            if not valid:
                break

        if valid:
            middle_pg_sum += int(update[len_up // 2])
        else:
            invalid_updates.append(update)

    return middle_pg_sum, invalid_updates


def part2(invalid_updates):
    middle_pg_sum = 0
    for iu in invalid_updates:
        for j in range(len(iu) - 1):
            for k in range(j + 1, len(iu)):
                if iu[k] not in rules[iu[j]]:
                    temp = iu[k]
                    iu[k] = iu[j]
                    iu[j] = temp
        middle_pg_sum += int(iu[len(iu) // 2])

    return middle_pg_sum


ans_part_1, invalid_updates = part1()
ans_part_2 = part2(invalid_updates)

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 5948
assert ans_part_2 == 3062
