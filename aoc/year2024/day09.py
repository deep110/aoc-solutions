from typing import List
from aoc.utils import read_input

ms = read_input(2024, 9)


class File:
    def __init__(self, id, size, empty_len=0, empty_start_index=-1):
        self.id = id
        self.size = size
        self.empty_len = empty_len
        self.empty_start_index = empty_start_index
        self.content = [id] * size

    def fill(self, target_file: "File"):
        self.content[
            self.empty_start_index : self.empty_start_index + target_file.size
        ] = target_file.content
        self.empty_len -= target_file.size
        self.empty_start_index += target_file.size

    def empty(self):
        self.content = ["."] * self.size
        self.empty_len = self.size
        self.empty_start_index = 0

    def __repr__(self):
        return f"<{self.content}>"


def part1():
    file_id = 0
    disk = []

    for i in range(len(ms)):
        block = int(ms[i])
        if i % 2 == 0:
            disk.extend([str(file_id)] * block)
            file_id += 1
        else:
            disk.extend(["."] * block)

    k = 0
    for j in range(len(disk) - 1, -1, -1):
        if j == k:
            break
        if disk[j] != ".":
            while j > k:
                if disk[k] == ".":
                    disk[k] = disk[j]
                    disk[j] = "."
                    break
                else:
                    k += 1

    checksum = 0
    for i, d in enumerate(disk):
        if d == ".":
            break
        checksum += i * int(d)
    return checksum


def part2():
    file_id = 0
    disk: List[File] = []
    file_index = []
    memo = [0] * 10

    for i in range(len(ms)):
        block = int(ms[i])
        if i % 2 == 0:
            file_index.append(len(disk))
            disk.append(File(str(file_id), block))
            file_id += 1
        else:
            if block != 0:
                f = File(".", block, empty_len=block, empty_start_index=0)
                disk.append(f)
    file_index.reverse()

    for j in file_index:
        file_block: File = disk[j]

        # find an empty block that can fit it
        start_idx = memo[file_block.size]
        if start_idx is None:
            continue

        for k in range(start_idx, j):
            to_check_block = disk[k]
            if to_check_block.empty_len >= file_block.size:
                to_check_block.fill(file_block)

                # we set the memo to the file size we found, since all the files
                # before this had less empty space than this size
                memo[file_block.size] = k
                file_block.empty()
                break

            if k == j - 1:
                memo[file_block.size] = None

    checksum = 0
    idx = 0
    for f in disk:
        for d in f.content:
            if d != ".":
                checksum += idx * int(d)
            idx += 1
    return checksum


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 6349606724455
assert ans_part_2 == 6376648986651
