from aoc.utils import read_input

ms = read_input(2018, 5).rstrip()


def part1(ms: str):
    processed_polymer = []
    for p in ms:
        if (
            len(processed_polymer) > 0
            and abs(ord(p) - ord(processed_polymer[-1])) == 32
        ):
            processed_polymer.pop()
        else:
            processed_polymer.append(p)

    return len(processed_polymer)


def part2(ms: str):
    least_len = 100000
    for i in range(ord("a"), ord("z")):
        p = ms.replace(chr(i), "").replace(chr(i - 32), "")
        processed_len = part1(p)
        if processed_len < least_len:
            least_len = processed_len

    return least_len


ans_part_1 = part1(ms)
ans_part_2 = part2(ms)

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 9116
assert ans_part_2 == 6890
