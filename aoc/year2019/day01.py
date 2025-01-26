"""
# The Tyranny of the Rocket Equation

The title of the problem is a reference to the
[real life equation](https://en.wikipedia.org/wiki/Tsiolkovsky_rocket_equation).
"""

from aoc.utils import read_input

ms = read_input(2019, 1).split("\n")


def calc_total_fr(mass: int):
    fuel = 0
    while mass > 8:
        mass = mass // 3 - 2
        fuel += mass
    return fuel


def part12():
    base_mass = 0
    full_mass = 0

    for m in ms:
        m = int(m)
        base_mass += m // 3 - 2
        full_mass += calc_total_fr(m)

    return base_mass, full_mass


ans_part_1, ans_part_2 = part12()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 3273715
assert ans_part_2 == 4907702
