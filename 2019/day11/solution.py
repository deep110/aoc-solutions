from collections import defaultdict
from os import path
import sys

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from intcode_computer import IntCodeComputer

#              UP,     RIGHT,   DOWN,     LEFT
DIRECTIONS = [(0, -1), (1, 0), (0, 1), (-1, 0)]
ALPHABET_6 = {
    ".##.\n#..#\n#..#\n####\n#..#\n#..#": "A",
    "###.\n#..#\n###.\n#..#\n#..#\n###.": "B",
    ".##.\n#..#\n#...\n#...\n#..#\n.##.": "C",
    "####\n#...\n###.\n#...\n#...\n####": "E",
    "####\n#...\n###.\n#...\n#...\n#...": "F",
    ".##.\n#..#\n#...\n#.##\n#..#\n.###": "G",
    "#..#\n#..#\n####\n#..#\n#..#\n#..#": "H",
    ".###\n..#.\n..#.\n..#.\n..#.\n.###": "I",
    "..##\n...#\n...#\n...#\n#..#\n.##.": "J",
    "#..#\n#.#.\n##..\n#.#.\n#.#.\n#..#": "K",
    "#...\n#...\n#...\n#...\n#...\n####": "L",
    ".##.\n#..#\n#..#\n#..#\n#..#\n.##.": "O",
    "###.\n#..#\n#..#\n###.\n#...\n#...": "P",
    "###.\n#..#\n#..#\n###.\n#.#.\n#..#": "R",
    ".###\n#...\n#...\n.##.\n...#\n###.": "S",
    "#..#\n#..#\n#..#\n#..#\n#..#\n.##.": "U",
    "#...\n#...\n.#.#\n..#.\n..#.\n..#.": "Y",
    "####\n...#\n..#.\n.#..\n#...\n####": "Z",
}

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ss = list(map(lambda x: int(x), f.read().split(",")))


def convert_6(array: list[list[str]]) -> str:
    # Validate input
    rows, cols = len(array), len(array[0])
    if any(len(row) != cols for row in array):
        raise ValueError("all rows should have the same number of columns")
    if rows != 6:
        raise ValueError("incorrect number of rows (expected 6)")

    # Convert each letter
    indices = [slice(start, start + 4) for start in range(0, cols, 5)]
    result = [
        ALPHABET_6["\n".join("".join(row[index]) for row in array)] for index in indices
    ]

    return "".join(result)


def run_program(instructions, start_coord_color: int):
    panels = defaultdict(int)
    curr_cord = (0, 0)
    panels[curr_cord] = start_coord_color
    curr_dir_idx = 0
    computer = IntCodeComputer(instructions, extra_memory=500)

    while True:
        # run program
        color = computer.run_program(panels[curr_cord])
        # break here, since computer can halt at color step,
        # because of this we have a lingering dot
        if computer.is_halted:
            break
        turn_idx = computer.run_program()

        panels[curr_cord] = color
        if turn_idx == 1:
            curr_dir_idx = (curr_dir_idx + 1) % 4
        else:
            curr_dir_idx = (curr_dir_idx - 1) % 4

        di, dj = DIRECTIONS[curr_dir_idx]
        curr_cord = curr_cord[0] + di, curr_cord[1] + dj

    return panels


def get_bounds(coords):
    min_x = 1000000
    min_y = 1000000
    max_x = -1000000
    max_y = -1000000

    for x, y in coords:
        if x < min_x:
            min_x = x
        if y < min_y:
            min_y = y
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y

    return min_x, min_y, max_x, max_y


def part1():
    panels = run_program(ss.copy(), 0)
    return len(panels.keys())


def part2():
    panels = run_program(ss, 1)
    white_panels = []
    for c, color in panels.items():
        if color == 1:
            white_panels.append(c)

    min_x, min_y, max_x, max_y = get_bounds(white_panels)
    width = max_x - min_x + 1
    height = max_y - min_y + 1

    grid = []
    for _ in range(height):
        grid.append(["."] * width)

    for x, y in white_panels:
        grid[y - min_y][x - min_x] = "#"

    return convert_6(grid)


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 1885
assert ans_part_2 == "BFEAGHAF"
