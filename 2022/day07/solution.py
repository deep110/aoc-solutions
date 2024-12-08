from os import path
import re
import math

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

COMMAND = re.compile(r"\$ (ls|cd) ?(.*)")
FILE = re.compile(r"(dir|\d+) (.*)")
TOTAL_SPACE = 70000000
UPDATE_SIZE = 30000000


class File:
    def __init__(self, name, size=0, is_dir=False):
        self.name = str(name)
        self.is_dir = is_dir
        self.size = size
        self.parent = None
        self.child = []

    def __repr__(self):
        return self.name

    def get_size(self):
        if self.size != 0:
            return self.size

        size = 0
        for c in self.child:
            if c.is_dir and c.size == 0:
                size += c.get_size()
            else:
                size += c.size

        self.size = size
        return size

    def in_child(self, file_name):
        for i in self.child:
            if i.name == file_name:
                return i


def change_dir(new_dir_name, current_dir, fs):
    if new_dir_name == "..":
        if current_dir.name == "/":
            return current_dir
        return current_dir.parent

    if new_dir_name == "/":
        return fs[0]

    return current_dir.in_child(new_dir_name)


def add_file(input, current_dir, fs):
    m = FILE.match(input)
    if current_dir.in_child(m[2]):
        return

    if m[1] == "dir":
        new_file = File(m[2], 0, is_dir=True)
        fs.append(new_file)
    else:
        new_file = File(m[2], int(m[1]))

    new_file.parent = current_dir
    current_dir.child.append(new_file)


def build_file_system():
    fs = [File("/", 0, True)]
    current_dir = None

    for i in ms:
        # if it is command
        if i[0] == "$":
            m = COMMAND.match(i)
            if m[1] == "cd":
                current_dir = change_dir(m[2], current_dir, fs)
                if current_dir is None:
                    raise Exception(f"No dir found - {current_dir}")
        else:
            add_file(i, current_dir, fs)

    for d in fs:
        d.get_size()

    return fs


fs = build_file_system()


def part1():
    total = 0
    for d in fs:
        size = d.get_size()
        if size < 100000:
            total += size

    return total


def part2():
    used_space = fs[0].size
    free_space = TOTAL_SPACE - used_space
    space_needed = UPDATE_SIZE - free_space

    deleted_size = math.inf
    for d in fs:
        s = d.get_size()
        if s >= space_needed and s < deleted_size:
            deleted_size = s

    return deleted_size


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 1084134
assert ans_part_2 == 6183184
