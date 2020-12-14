from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

ms = list(map(lambda x: int(x), ms))

PREAMBLE_LEN = 25

def is_sum_exists(num, array_inputs):
    for i in range(0, len(array_inputs)):
        diff = num - array_inputs[i]
        if diff > 0:
            for j in range(i+1, len(array_inputs)):
                if diff == array_inputs[j]:
                    return True
    return False

def part1():
    invalid_num = -1
    for i, num in enumerate(ms[PREAMBLE_LEN:]):
        # since index starts from preamble_length
        nums = ms[i:i + PREAMBLE_LEN]
        is_ex = is_sum_exists(num, nums)
        if not is_ex:
            invalid_num = num
            break

    return invalid_num


def part2(invalid_num):
    si, ei = (0, 0)
    _sum = 0
    for i in range(0, len(ms)):
        _sum += ms[i]
        while _sum > invalid_num:
            _sum -= ms[si]
            si += 1
        if _sum == invalid_num:
            ei = i
            break

    _range = ms[si:ei+1]
    return min(_range) + max(_range)


invalid_num = part1()
print("Part1 solution: ", invalid_num)
print("Part2 solution: ", part2(invalid_num))  