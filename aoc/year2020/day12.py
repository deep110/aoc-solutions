"""
# Rain Risk

Part2, required vector rotation, since angles are multiples of 90°, we can avoid
trigonometric functions, using complex algebra.
- For clockwise, i.e right, Its like multiplying by -i in complex algebra
- For anti-clockwise, i.e left, Its like multiplying by i in complex algebra
"""

from aoc.utils import read_input

instructions = read_input(2020, 12).split("\n")
DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def part1():
    ci, cj = (0, 0)  # current position
    di, dj = (1, 0)  # current direction
    dir_index = 2

    for instruction in instructions:
        action = instruction[:1]
        value = int(instruction[1:])

        match action:
            case "F":
                ci += di * value
                cj += dj * value
            case "N":
                cj += value
            case "S":
                cj -= value
            case "E":
                ci += value
            case "W":
                ci -= value
            case "L":
                dir_index = (dir_index - value // 90) % 4
                di, dj = DIRS[dir_index]
            case "R":
                dir_index = (dir_index + value // 90) % 4
                di, dj = DIRS[dir_index]

    return abs(ci) + abs(cj)


def part2():
    ci, cj = (0, 0)  # current position
    wi, wj = (10, 1)  # waypoint

    for instruction in instructions:
        action = instruction[:1]
        value = int(instruction[1:])

        match action:
            case "F":
                ci += wi * value
                cj += wj * value
            case "N":
                wj += value
            case "S":
                wj -= value
            case "E":
                wi += value
            case "W":
                wi -= value
            case "L":
                for _ in range(0, value // 90):
                    wi, wj = -wj, wi
            case "R":
                for _ in range(0, value // 90):
                    wi, wj = wj, -wi

    return abs(ci) + abs(cj)


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 938
assert ans_part_2 == 54404
