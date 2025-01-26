"""
# Secure Container

We speed things up by only checking numbers that have digits in non-decreasing order for pairs.
These numbers become rapidly less dense as the password value increases.
"""

from collections import Counter

RANGE_MIN = 372304
RANGE_MAX = 847060


class IncNum:
    def __init__(self, input_num):
        # Convert an integer to our 6-digit format
        d0 = (input_num // 100_000) % 10
        d1 = (input_num // 10_000) % 10
        d2 = (input_num // 1_000) % 10
        d3 = (input_num // 100) % 10
        d4 = (input_num // 10) % 10
        d5 = input_num % 10

        self.digits = [d0, d1, d2, d3, d4, d5]

    # maybe be increasing
    def inc(self):
        # Increment the number while maintaining increasing order
        for i in range(5, -1, -1):  # Iterate from 5 down to 0
            self.digits[i] += 1
            if self.digits[i] != 10:
                return

            # Only runs if we hit 10
            if i == 0:
                self.digits[i] = 0
            else:
                self.digits[i] = self.digits[i - 1]

    def to_str(self):
        return "".join(map(str, self.digits))


def is_increase(digits: str):
    for i in range(1, 6):
        if digits[i] < digits[i - 1]:
            return False
    return True


def part12():
    part1 = 0
    part2 = 0

    num = IncNum(RANGE_MIN)
    max_str = str(RANGE_MAX)

    while True:
        num.inc()
        num_str = num.to_str()

        if num_str > max_str:
            break

        if is_increase(num_str) and len(set(num_str)) < 6:
            part1 += 1
            if 2 in Counter(num_str).values():
                part2 += 1

    return part1, part2


ans_part_1, ans_part_2 = part12()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 475
assert ans_part_2 == 297
