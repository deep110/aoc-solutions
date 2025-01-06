from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

numbers = list(map(lambda x: int(x), ms))

MASK = 16777215  # 2 ^ 24 - 1
DIV = 19**4


def part12():
    total_sum = 0
    num_changes = 2000
    # all_sequences_total_bananas = defaultdict(int)
    all_sequences_total_bananas = [0] * DIV
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

        # converts into 4 bits of base 19 since there are 19 unique values
        # 19^3 * (seq[3] + 9) + 19^2 * (seq[2] + 9) + 19 * (seq[1] + 9) + (seq[0] + 9)
        #
        # since we dont care of exact value just unique value, we can avoid adding 9

        key = delta[0] * 361 + delta[1] * 19 + delta[2]
        for i in range(3, num_changes):
            key = (key * 19 + delta[i]) % DIV
            if key not in seen_seq:
                all_sequences_total_bananas[key] += price[i + 1]
                seen_seq.add(key)

        total_sum += sn

    return total_sum, max(all_sequences_total_bananas)


ans_part_1, ans_part_2 = part12()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 18941802053
assert ans_part_2 == 2218
