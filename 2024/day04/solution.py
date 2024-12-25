from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

ms = list(map(lambda x: x.strip(), ms))


def part1():
    num_xmas = 0

    len_row = len(ms[0])
    len_column = len(ms)

    for i in range(len_column):
        for j in range(len_row):
            if ms[i][j] == "X":
                # search right
                if j + 3 <= len_row - 1 and ms[i][j + 1 : j + 4] == "MAS":
                    num_xmas += 1

                # search left
                if j - 3 >= 0 and ms[i][j - 3 : j + 1] == "SAMX":
                    num_xmas += 1

                # search top
                if i - 3 >= 0 and ms[i - 3][j] + ms[i - 2][j] + ms[i - 1][j] == "SAM":
                    num_xmas += 1

                # search bottom
                if (
                    i + 3 <= len_column - 1
                    and ms[i + 1][j] + ms[i + 2][j] + ms[i + 3][j] == "MAS"
                ):
                    num_xmas += 1

                # search right-bottom diagonal
                if (
                    i + 3 <= len_column - 1
                    and j + 3 <= len_row - 1
                    and ms[i + 1][j + 1] + ms[i + 2][j + 2] + ms[i + 3][j + 3] == "MAS"
                ):
                    num_xmas += 1

                # search left-bottom diagonal
                if (
                    i + 3 <= len_column - 1
                    and j - 3 >= 0
                    and ms[i + 1][j - 1] + ms[i + 2][j - 2] + ms[i + 3][j - 3] == "MAS"
                ):
                    num_xmas += 1

                # search right-top diagonal
                if (
                    i - 3 >= 0
                    and j + 3 <= len_row - 1
                    and ms[i - 1][j + 1] + ms[i - 2][j + 2] + ms[i - 3][j + 3] == "MAS"
                ):
                    num_xmas += 1

                # search left-top diagonal
                if (
                    i - 3 >= 0
                    and j - 3 >= 0
                    and ms[i - 1][j - 1] + ms[i - 2][j - 2] + ms[i - 3][j - 3] == "MAS"
                ):
                    num_xmas += 1

    return num_xmas


def part2():
    num_x_mas = 0

    len_row = len(ms[0])
    len_column = len(ms)

    for i in range(len_column):
        for j in range(len_row):
            if ms[i][j] == "A":
                if (
                    i - 1 >= 0
                    and i + 1 <= len_column - 1
                    and j - 1 >= 0
                    and j + 1 <= len_row - 1
                    and ms[i - 1][j - 1] + ms[i + 1][j + 1] in ["MS", "SM"]
                    and ms[i - 1][j + 1] + ms[i + 1][j - 1] in ["MS", "SM"]
                ):
                    num_x_mas += 1

    return num_x_mas


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 2642
assert ans_part_2 == 1974
