from os import path
from collections import Counter

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

a = list(map(lambda x: x.rstrip("\n"), ms))

def part1():
    twos = 0
    threes = 0

    for i in a:
        q = Counter(i)
        vals = list(q.values())
        if 2 in vals:
            twos += 1

        if 3 in vals:
            threes += 1

    ans = twos * threes
    return ans

def is_correct(str1, str2):
    def if_one_diff(_s1, _s2):
        k = 0
        for i, j in zip(_s1, _s2):
            if not (i == j):
                k += 1
            if k > 1:
                return False
        return True

    if str1[:len(str1) // 2] == str2[:len(str2) // 2]:
        return if_one_diff(str1[len(str1) // 2:], str2[len(str2) // 2:])
    else:
        if str1[len(str1) // 2:] == str2[len(str2) // 2:]:
            return if_one_diff(str1[:len(str1) // 2], str2[:len(str2) // 2])
        else:
            return False


def get_ans(str1, str2):
    ans = ''
    for i, j in zip(str1, str2):
        if i == j:
            ans += i

    return ans

def part2():
    for i in a:
        for j in a:
            if (not (i == j)) and is_correct(i, j):
                return get_ans(i, j)

print("Part1 solution: ", part1())
print("Part2 solution: ", part2())
