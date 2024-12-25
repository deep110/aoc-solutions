from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

towels = ms[0].strip().split(", ")


def design_possible_count(design, index, cache):
    if index == len(design):
        return 1

    if design[index:] in cache:
        return cache[design[index:]]

    count = 0
    for towel in towels:
        if towel == design[index : index + len(towel)]:
            kc = design_possible_count(design, index + len(towel), cache)
            count += kc

    cache[design[index:]] = count
    return count


def part12():
    total_possible = 0
    total_possible_count = 0

    for arrangement in ms[2:]:
        arrangement = arrangement.strip()
        cache = {}

        count = design_possible_count(arrangement, 0, cache)
        total_possible_count += count
        if count > 0:
            total_possible += 1

    return total_possible, total_possible_count


ans_part_1, ans_part_2 = part12()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 269
assert ans_part_2 == 758839075658876
