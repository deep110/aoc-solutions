"""
# Day 8: Seven Segment Search

For Part2, I for length 5 and 6, we can uniquely determine the digits by taking
intersection of segments with segments of 1 and 4.
"""

from aoc.utils import read_input


displays = []
for _input in read_input(2021, 8).split("\n"):
    k = tuple(i.split(" ") for i in _input.split(" | "))
    displays.append(k)


def part1():
    num_times = 0
    for out in displays:
        num_times += sum(map(lambda x: len(x) < 5 or len(x) == 7, out[1]))

    return num_times


def part2():
    ans_p2 = 0
    for signals, output in displays:
        # we only need to know segments in 1 (len_seg == 2) and 4 (len_seg == 4)
        len_to_segment = {len_s: set(s) for s in signals if (len_s := len(s)) in (2, 4)}

        num = ""
        for out in output:
            len_s = len(out)
            if len_s == 2:
                num += "1"
            elif len_s == 3:
                num += "7"
            elif len_s == 4:
                num += "4"
            elif len_s == 7:
                num += "8"
            elif len_s == 5:
                set_out = set(out)
                if len(set_out & len_to_segment[2]) == 2:
                    num += "3"
                elif len(set_out & len_to_segment[4]) == 2:
                    num += "2"
                else:
                    num += "5"
            else:  # len_s == 6
                set_out = set(out)
                if len(set_out & len_to_segment[4]) == 4:
                    num += "9"
                elif len(set_out & len_to_segment[2]) == 1:
                    num += "6"
                else:
                    num += "0"

        ans_p2 += int(num)

    return ans_p2


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution:", ans_part_1)
print("Part2 solution:", ans_part_2)

assert ans_part_1 == 245
assert ans_part_2 == 983026
