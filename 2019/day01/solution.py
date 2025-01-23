from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()


def calc_total_fr(mass: int):
    t = 0
    while mass > 3:
        fr = mass // 3 - 2
        if fr > 0:
            t += fr
        mass = fr
    return t


def part12():
    base_mass = 0
    full_mass = 0

    for m in ms:
        m = int(m.strip())
        base_mass += m // 3 - 2
        full_mass += calc_total_fr(m)

    return base_mass, full_mass


ans_part_1, ans_part_2 = part12()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 3273715
assert ans_part_2 == 4907702
