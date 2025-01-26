from collections import Counter
from aoc.utils import read_input, image_arr_to_str


ins = read_input(2019, 8).rstrip()

WIDTH = 25
HEIGHT = 6
LAYER_LENGTH = WIDTH * HEIGHT


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

    return image_arr_to_str(final_img)


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 1088
assert ans_part_2 == "LGYHB"
