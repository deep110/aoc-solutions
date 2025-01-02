input_str = "0,3,1,6,7,5"
input = list(map(lambda x: int(x), input_str.split(",")))

ARR_THRESHOLD = 10_000_000


def part12(number_idx):
    # deliberately use an array instead of map, since array lookups are faster
    turn_arr_cache = [None] * min(number_idx, ARR_THRESHOLD)
    turn_dict_cache = {}

    for i in range(len(input)):
        turn_arr_cache[input[i]] = i + 1

    last_number = 0
    for turn_num in range(len(input) + 1, number_idx):
        if last_number < ARR_THRESHOLD:
            val = turn_arr_cache[last_number]
            turn_arr_cache[last_number] = turn_num
        else:
            val = turn_dict_cache.get(last_number)
            turn_dict_cache[last_number] = turn_num

        last_number = turn_num - val if val else 0

    return last_number


ans_part_1 = part12(2020)
ans_part_2 = part12(30_000_000)

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 852
assert ans_part_2 == 6007666
