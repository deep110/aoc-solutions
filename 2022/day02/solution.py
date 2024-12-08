from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.read().split("\n")

ms = list(filter(lambda x: len(x) > 0, ms))


def part1():
    WIN_CONDITION = ["A Y", "B Z", "C X"]
    DRAW_CONDITION = ["A X", "B Y", "C Z"]

    score = 0
    for game in ms:
        score += ord(game[-1]) - 87
        if game in WIN_CONDITION:
            score += 6
        elif game in DRAW_CONDITION:
            score += 3

    return score


def part2():
    score = 0

    for game in ms:
        win_score = (ord(game[-1]) - 88) * 3
        shape_score = 0

        elf_shape = ord(game[0]) - 64
        if game[-1] == "X":
            shape_score = (elf_shape + 2) % 3
        elif game[-1] == "Y":
            shape_score = elf_shape
        else:
            shape_score = (elf_shape + 1) % 3
        if shape_score == 0:
            shape_score = 3

        score += shape_score + win_score

    return score


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 11475
assert ans_part_2 == 16862
