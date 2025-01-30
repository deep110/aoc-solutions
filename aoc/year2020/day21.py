from typing import Dict
from aoc.utils import read_input


def parse_input():
    ms = read_input(2020, 21).split("\n")
    foods = []
    allergens = []
    for m in ms:
        out = m.rsplit(" (contains ")
        foods.append(set(out[0].split(" ")))
        allergens.append(out[1].removesuffix(")").split(", "))

    return foods, allergens


foods, allergens = parse_input()


def part1():
    allergen_map: Dict[str, set] = {}
    for food, maybe_allergens in zip(foods, allergens):
        for allergen in maybe_allergens:
            if allergen in allergen_map:
                allergen_map[allergen] = allergen_map[allergen] & food
            else:
                allergen_map[allergen] = food

    removed_set = set()
    food_allergen = {}
    while allergen_map:
        # Find allergen with only one possible food after removing assigned foods
        for alg, values in allergen_map.items():
            remaining = values - removed_set
            if len(remaining) == 1:
                food = remaining.pop()
                food_allergen[alg] = food
                removed_set.add(food)
                del allergen_map[alg]
                break

    count = 0
    allergen_foods = set(food_allergen.values())
    for f in foods:
        count += len(f - allergen_foods)

    return count, food_allergen


def part2(food_allergen: Dict[str, str]):
    print(food_allergen)
    items = []
    for _, food in sorted(food_allergen.items(), key=lambda v: v[0]):
        items.append(food)

    return ",".join(items)


ans_part_1, food_allergen = part1()
ans_part_2 = part2(food_allergen)

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 2798
assert ans_part_2 == "gbt,rpj,vdxb,dtb,bqmhk,vqzbq,zqjm,nhjrzzj"
