from collections import defaultdict
from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

numbers = list(map(lambda x: int(x), ms))

MASK = 16777216 - 1  # 2 ^ 24 - 1


def part1():
    total_sum = 0
    all_prices = []

    for num in numbers:
        sn = num
        price = [sn % 10]
        for _ in range(2000):
            sn = ((sn << 6) ^ sn) & MASK
            sn = ((sn >> 5) ^ sn) & MASK
            sn = ((sn << 11) ^ sn) & MASK
            price.append(sn % 10)

        all_prices.append(price)
        total_sum += sn

    return total_sum, all_prices


def part2(prices):
    num_monkeys = len(prices)
    num_changes = 2000
    all_sequences_total_bananas = defaultdict(int)

    delta = [0] * num_changes
    for m in range(num_monkeys):
        seen_seq = set()
        price = prices[m]
        for i in range(0, num_changes):
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

    return max(all_sequences_total_bananas.values())


ans_part_1, prices = part1()
ans_part_2 = part2(prices)

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 18941802053
assert ans_part_2 == 2218
