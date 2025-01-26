from aoc.utils import read_input

ms = read_input(2024, 22).split("\n")
numbers = list(map(lambda x: int(x), ms))

MASK = 16777215  # 2 ^ 24 - 1
LIST_LENGTH = 19**4


def part12():
    part1_sum = 0

    # Idea of using arrays with base-19 index which would be
    #   faster than the dictionary is from Reddit user u/notrom11,
    #   though in Python 3.11, 3.12, 3.13 lists are faster
    #   so reverted them to lists
    all_sequences_total_bananas = [0] * LIST_LENGTH
    idx_change_seq_list = [0] * LIST_LENGTH

    for idx_s, num in enumerate(numbers):
        next_idx_s = idx_s + 1
        sn = num
        prev_price = 0
        prev_idx_change_seq = 0

        for i in range(2000):
            sn = ((sn << 6) ^ sn) & MASK
            # No need to bit mask since right shifting ensures that it is always 24 bits
            sn = (sn >> 5) ^ sn
            sn = ((sn << 11) ^ sn) & MASK

            # Instead of shifting the sequence of changes which we end up just using
            #   as an index, we instead compute the index straight away, and shifting
            #   is done by simply dividing the previous index by 19, and then adding
            #   the new change scaled by 19**3
            # This is equivalent to the following, but without needing to track changes:
            #   changes_list[0:4] = changes_list[1:4] + [change]
            #   idx_change_seq = changes_list[3]*(19**3) + \
            #                    changes_list[2]*(19**2) + \
            #                    changes_list[1]*19 + \
            #                    changes_list[0]
            price = sn % 10
            if i == 0:
                # change = 0, so set index to 0
                idx_change_seq = 0
            else:
                # Offset by 9 since change is -9 to +9, still works
                #   without offsets due to negative indices but is slower
                # change = (d - prev_d) + 9 then scale by 19**3 = 6859
                idx_change_seq = ((price - prev_price) + 9) * 6859 + (
                    prev_idx_change_seq // 19
                )
            prev_price = price
            prev_idx_change_seq = idx_change_seq

            # If there have been a sequence of 4 changes, and the sequence hasn't been seen
            # Instead of marking the sequence as seen or not and clearing them for each new
            # secret_num, set it to the index+1 whenever its seen to prevent need for clearing
            if i >= 4 and idx_change_seq_list[idx_change_seq] <= idx_s:
                idx_change_seq_list[idx_change_seq] = next_idx_s
                all_sequences_total_bananas[idx_change_seq] += price

        part1_sum += sn

    return part1_sum, max(all_sequences_total_bananas)


ans_part_1, ans_part_2 = part12()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 18941802053
assert ans_part_2 == 2218
