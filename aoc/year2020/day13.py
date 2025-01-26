from aoc.utils import read_input

ms = read_input(2020, 13).split("\n")


def mod_inv(num, value):
    """
    (value * mod_inv) % num = 1

    Example: num = 3, value = 20
    then mod_inv = 2

    (20 * 2) % 3 = 1
    """
    inv = 1
    while True:
        if (value * inv) % num == 1:
            return inv
        inv += 1


def part1():
    start_timestamp = int(ms[0])
    timestamp = start_timestamp
    bus_ids = list(
        map(lambda x: int(x), filter(lambda x: x != "x", ms[1].split(",")))
    )

    while True:
        for bus_id in bus_ids:
            if timestamp % bus_id == 0:
                return (timestamp - start_timestamp) * bus_id

        timestamp += 1


def part2():
    """
    We are going to use chinese remainder theorem.
    """
    numbers = []
    remainders = []
    product = 1

    for i, bid in enumerate(ms[1].strip().split(",")):
        if bid != "x":
            bid = int(bid)
            numbers.append(bid)
            remainders.append(bid - i % bid)
            product *= bid

    result = 0
    for i in range(len(numbers)):
        ppi = product // numbers[i]

        # inv(i) = Modular Multiplicative Inverse of pp[i] with respect to num[i]
        result += ppi * remainders[i] * mod_inv(numbers[i], ppi)

    return result % product


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 3385
assert ans_part_2 == 600689120448303
