from collections import Counter
from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ins = f.read().strip()

WIDTH = 25
HEIGHT = 6
LAYER_LENGTH = WIDTH * HEIGHT
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


def part1():
    req_layer_counter = {"0": LAYER_LENGTH}

    for i in range(0, len(ins), LAYER_LENGTH):
        layer_counter = Counter(ins[i : i + LAYER_LENGTH])
        if layer_counter["0"] < req_layer_counter["0"]:
            req_layer_counter = layer_counter

    return req_layer_counter["1"] * req_layer_counter["2"]


def part2():
    bit_map = {"0": ".", "1": "#"}
    final_img = []
    for i in range(HEIGHT):
        row = []
        for j in range(WIDTH):
            k = j + i * WIDTH
            # find the bit which is required
            final_bit = "."
            layer_num = 0
            while True:
                layer_bit = ins[k + layer_num * LAYER_LENGTH]
                if layer_bit == "2":
                    layer_num += 1
                else:
                    final_bit = bit_map[layer_bit]
                    break

            row.append(final_bit)
        final_img.append(row)

    return convert_6(final_img)


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 1088
assert ans_part_2 == "LGYHB"
