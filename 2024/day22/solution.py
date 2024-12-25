from collections import defaultdict
from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

numbers = list(map(lambda x: int(x), ms))

MASK = 16777216 - 1  # 2 ^ 24 - 1


def part12():
    total_sum = 0
    num_monkeys = len(numbers)
    num_changes = 2000
    all_sequences_total_bananas = defaultdict(int)
    delta = [0] * num_changes

    for num in numbers:
        sn = num
        price = [sn % 10]
        seen_seq = set()

        for i in range(2000):
            sn = ((sn << 6) ^ sn) & MASK
            # we can remove AND since,
            # the result of the first prune step is guaranteed to be below 2^24,
            # the second prune step is a no-op
            sn = (sn >> 5) ^ sn
            sn = ((sn << 11) ^ sn) & MASK
            price.append(sn % 10)
            delta[i] = price[i + 1] - price[i]

        # converts into 4 bits of base 20 since there are 19 unique values
        #
        # 20^3 * (seq[3] + 10) + 20^2 * (seq[2] + 10) + 20 * (seq[1] + 10) + (seq[0] + 10)

        # but with few optimizations, since we dont care of exact value just unique value,
        # we can avoid adding 10
        for i in range(4, num_changes + 1):
            key = (
                8000 * delta[i - 4]
                + 400 * delta[i - 3]
                + 20 * delta[i - 2]
                + delta[i - 1]
            )
            if key not in seen_seq:
                all_sequences_total_bananas[key] += price[i]
                seen_seq.add(key)

        total_sum += sn

    return total_sum, max(all_sequences_total_bananas.values())


ans_part_1, ans_part_2 = part12()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 18941802053
assert ans_part_2 == 2218
