from os import path
import re

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

COMMAND = re.compile(r"(addx|noop) ?(.*)")

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


def _convert_6(array: list[list[str]]) -> str:
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


def part1():
    X = 1
    num_cycles = 220
    pc = 0
    add_in_progress = False
    total = 0

    for i in range(1, num_cycles + 1):
        if i in [20, 60, 100, 140, 180, 220]:
            total += i * X

        mt = COMMAND.search(ms[pc])
        if mt[1] == "noop":
            pc += 1
        else:
            if add_in_progress:
                X += int(mt[2])
                add_in_progress = False
                pc += 1
            else:
                add_in_progress = True
    return total


def part2():
    X = 1
    num_cycles = 240
    pc = 0
    add_in_progress = False
    rows = []
    for i in range(20):
        rows.append("")

    for c in range(num_cycles):
        cp = c % 40

        pixel = "."
        if cp >= X - 1 and cp <= X + 1:
            # pixel = "█"
            pixel = "#"
        rows[int(c / 40)] += pixel

        mt = COMMAND.search(ms[pc])
        if mt[1] == "noop":
            pc += 1
        else:
            if add_in_progress:
                X += int(mt[2])
                add_in_progress = False
                pc += 1
            else:
                add_in_progress = True

    prepared_array = list(filter(lambda x: len(x) > 0, rows))
    res = _convert_6(prepared_array)

    return res


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 16880
assert ans_part_2 == "RKAZAJBR"
