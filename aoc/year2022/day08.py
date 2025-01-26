from aoc.utils import read_input

ms = read_input(2022, 8).split("\n")

NUM_ROWS = len(ms)
NUM_COLUMNS = len(ms[0])


def part1():
    # start with counting edge trees
    visible = NUM_ROWS * 2 + NUM_COLUMNS * 2 - 4

    # check for inner trees
    for i in range(1, NUM_ROWS - 1):
        for j in range(1, NUM_COLUMNS - 1):
            if max(ms[i][:j]) < ms[i][j]:  # look left
                visible += 1
                continue

            if max(ms[i][j + 1 :]) < ms[i][j]:  # look right
                visible += 1
                continue

            if max([x[j] for x in ms[:i]]) < ms[i][j]:  # look up
                visible += 1
                continue

            if max([x[j] for x in ms[i + 1 :]]) < ms[i][j]:  # look down
                visible += 1
                continue

    return visible


def part2():
    max_score = 0

    for i in range(1, NUM_ROWS - 1):
        for j in range(1, NUM_COLUMNS - 1):
            # see left
            s_left = j
            for x in range(j - 1, 0, -1):
                if ms[i][x] >= ms[i][j]:
                    s_left = j - x
                    break

            s_right = NUM_COLUMNS - j - 1
            for x in range(j + 1, NUM_COLUMNS, 1):
                if ms[i][x] >= ms[i][j]:
                    s_right = x - j
                    break

            s_up = i
            for x in range(i - 1, -1, -1):
                if ms[x][j] >= ms[i][j]:
                    s_up = i - x
                    break

            s_down = NUM_ROWS - i - 1
            for x in range(i + 1, NUM_ROWS, 1):
                if ms[x][j] >= ms[i][j]:
                    s_down = x - i
                    break

            scenic_score = s_left * s_right * s_up * s_down
            if scenic_score > max_score:
                max_score = scenic_score

    return max_score


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 1851
assert ans_part_2 == 574080
