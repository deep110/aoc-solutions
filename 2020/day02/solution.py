from os import path
import re

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

PATTERN = re.compile(r"([0-9]+)\-([0-9]+) ([a-z])\: (.*)")


def part1():
    no_valid = 0
    for i in ms:
        q = re.search(PATTERN, i)
        _min = int(q[1])
        _max = int(q[2])
        _letter = q[3]
        _password = q[4]

        count = _password.count(_letter)
        if count >= _min and count <= _max:
            no_valid += 1

    return no_valid


def part2():
    no_valid = 0
    for i in ms:
        q = re.search(PATTERN, i)
        _fi = int(q[1])
        _si = int(q[2])
        _letter = q[3]
        _password = q[4]

        a = _password[_fi - 1]
        b = _password[_si - 1]

        if (a == _letter and b != _letter) or (b == _letter and a != _letter):
            no_valid += 1

    return no_valid


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 434
assert ans_part_2 == 509
