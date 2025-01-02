from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms: list[str] = [x.strip() for x in f.readlines()]


towels_set = set(ms[0].split(", "))


def design_possible_count(design, cache) -> int:
    if design in cache:
        return cache[design]

    count = int(design in towels_set)
    for i in range(1, len(design)):
        if design[0:i] in towels_set:
            count += design_possible_count(design[i:], cache)

    cache[design] = count
    return count


def part12():
    total_possible = 0
    total_possible_count = 0

    cache = {}
    for arrangement in ms[2:]:
        count = design_possible_count(arrangement, cache)
        total_possible_count += count
        total_possible += int(count > 0)

    return total_possible, total_possible_count


ans_part_1, ans_part_2 = part12()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 269
assert ans_part_2 == 758839075658876
