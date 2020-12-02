import re
from collections import Counter

with open("input/input_2.txt") as f:
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

        pc = Counter(_password)
        count = pc[_letter]
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

        a = _password[_fi-1]
        b = _password[_si-1]

        if (a == _letter and b != _letter) or (b == _letter and a != _letter):
            no_valid += 1

    return no_valid

part2()
