from collections import defaultdict

input = "41078 18 7 0 4785508 535256 8154 447"


def stone_transformer(value):
    if len(value) % 2 == 0:
        hl = len(value) // 2
        return (value[:hl], str(int(value[hl:])))
    else:
        return (str(int(value) * 2024),)


def part_12(num_blinks: int):
    stones = defaultdict(int)
    stone_tf_map = defaultdict(list)
    stone_tf_map["0"] = ["1"]

    for i in input.split(" "):
        stones[i] += 1

    for nb in range(num_blinks):
        st_copy = {key: value for key, value in stones.items() if value > 0}
        for s in st_copy:
            # remove this stone from count
            num_stones = st_copy[s]
            stones[s] -= num_stones

            # transform this stone
            tr_val = stone_tf_map[s]
            if len(tr_val) == 0:
                tr_val = stone_transformer(s)
                stone_tf_map[s] = tr_val

            stones[tr_val[0]] += num_stones
            if len(tr_val) == 2:
                stones[tr_val[1]] += num_stones

    return sum(stones.values())


ans_part_1 = part_12(25)
ans_part_2 = part_12(75)

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 217443
assert ans_part_2 == 257246536026785
