from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

adapters = list(map(lambda x: int(x), ms))
adapters.sort()

# add power inlet and device outlet voltages
adapters.insert(0, 0)
adapters.append(adapters[-1] + 3)


def part1():
    # add one diff of 3, since our adapter also needs to be added which is
    # 3 higher than highest adapter value
    diff_map = {1: 0, 3: 0}

    for i in range(1, len(adapters)):
        diff = adapters[i] - adapters[i - 1]
        diff_map[diff] += 1

    return diff_map[1] * diff_map[3]


def part2():
    """
    Find pockets of diff of 3 and multiply all the arrangements of those segments
    """
    total_arrangements = 1
    pockets = []
    num_ones = 0
    for i in range(1, len(adapters)):
        diff = adapters[i] - adapters[i - 1]
        if diff == 3:
            pockets.append(num_ones)
            num_ones = 0
        else:
            num_ones += 1

    for pocket in pockets:
        if pocket <= 1:
            continue

        # we need to calculate total valid arrangements for this series of adapters
        # ideally it should be 2 ^ (number_of_diff_1)
        # but we cant have arrangement where all the third adapter is also absent, so we need to subtract that
        # from total arrangement
        #
        # total_arr = 2 ^ (num_diffs_1) - (every_third_is_absent)
        valid_pocket_len = pocket - 1
        every_third_is_absent_arr = 2 ** (valid_pocket_len // 3) - 1
        total_pocket_arr = 2**valid_pocket_len - every_third_is_absent_arr

        total_arrangements *= total_pocket_arr

    return total_arrangements


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 2400
assert ans_part_2 == 338510590509056
