"""
# Docking Data

Part1, is straightforward, we can use bitwise logic to get the correct value to write.

This method described below is directly inspired and ported from
https://github.com/maneatingape/advent-of-code-rust/blob/main/src/year2020/day14.rs

For Part2, The maximum number of Xs in any mask is 9 which
gives 2⁹ = 512 different memory addresses. A brute force solution will work, but there's a much
more elegant approach.

Key Concept: Instead of generating all possible addresses, we will treat each memory write
as a "set" of addresses and calculates overlaps between these sets.

Then by using the [inclusion-exclusion principle ](https://en.wikipedia.org/wiki/Inclusion%E2%80%93exclusion_principle)
we can determine any overlaps with other sets and deduct the correct number of values.

For example:
```none
    mask = 0000000000000000000000000000000001XX  // A
    mem[8] = 3
    mask = 00000000000000000000000000000000011X  // B
    mem[8] = 5
    mask = 000000000000000000000000000000000111  // C
    mem[8] = 7
```
Results in the following address sets:
```none
Set A: 12 13 14 15
Set B: 14 15
Set C: 15
```
Using the inclusion-exclusion principle the remaining size of A is:

4 (initial size) - 2 (overlap with B) - 1 (overlap with C) + 1 (overlap between B and C) = 2

To calculate the final answer we treat the value as the weight of the set, in this case:
2 * 3 + 1 * 5 + 1 * 7 = 18

The complexity of this approach depends on how many addresses overlap. For my input overlap
never went beyond two or three
"""

from dataclasses import dataclass
import re
from typing import Dict, List, Optional
from aoc.utils import read_input

ms = read_input(2020, 14).split("\n")


@dataclass
class Program:
    mask: str
    mem: Dict[int, int]
    mask_1_count: int = 0

    def calculate_1_0_masks(self):
        len_mask = len(self.mask)
        mask_1 = ["0"] * len_mask
        mask_0 = ["0"] * len_mask

        for i in range(len_mask):
            if self.mask[i] == "1":
                mask_1[i] = "1"
            elif self.mask[i] == "0":
                mask_0[i] = "1"

        # cache this part2
        self.mask_1_count = int("".join(mask_1), 2)

        return (int("".join(mask_0), 2), self.mask_1_count)


@dataclass
class Set:
    ones: int
    floating: int
    weight: int

    def intersect(self, other: "Set") -> Optional["Set"]:
        # Sets are disjoint if any 2 one bits are different and there is no X in either set
        disjoint = (self.ones ^ other.ones) & ~(self.floating | other.floating)

        if disjoint == 0:
            return Set(
                ones=self.ones | other.ones,
                floating=self.floating & other.floating,
                weight=0,
            )
        return None

    def size(self) -> int:
        return 1 << bin(self.floating).count("1")


def subsets(cube: Set, sign: int, candidates: List[Set]) -> int:
    total = 0
    for i, other in enumerate(candidates):
        if next_set := cube.intersect(other):
            total += sign * next_set.size() + subsets(
                next_set, -sign, candidates[i + 1 :]
            )
    return total


def parse_programs():
    MASK_PATTERN = re.compile(r"mask = (.*)")
    MEM_PATTERN = re.compile(r"mem\[(\d+)\] = (\d+)")

    programs = []
    program = None
    for m in ms:
        if m.startswith("mask"):
            program = Program(mask=MASK_PATTERN.match(m).group(1), mem={})
            programs.append(program)
        else:
            matched = MEM_PATTERN.match(m)
            program.mem[int(matched.group(1))] = int(matched.group(2))

    return programs


def part1(programs: List[Program]):
    global_mem = {}

    # we will go reverse, if memory is written, we skip it
    for i in range(len(programs) - 1, -1, -1):
        program = programs[i]
        mask_0, mask_1 = program.calculate_1_0_masks()

        for location, value in program.mem.items():
            if location in global_mem:
                continue

            # apply mask
            global_mem[location] = (value | mask_1) & ~mask_0

    return sum(global_mem.values())


def part2(programs: List[Program]):
    total = 0
    sets: List[Set] = []

    # Convert each memory write into a set
    for program in programs:
        # Convert mask to ones and floating bits
        ones = program.mask_1_count
        floating = int("".join("1" if c == "X" else "0" for c in program.mask), 2)

        # Create sets for each memory write under this mask
        for address, value in program.mem.items():
            # ones: places where both mask and address bit is one and not floating
            # floating: where X's are
            sets.append(
                Set(ones=(address | ones) & ~floating, floating=floating, weight=value)
            )

    # Process all sets using inclusion-exclusion principle
    for i, set_i in enumerate(sets):
        candidates = []
        # Find intersections with all later sets
        for j in range(i + 1, len(sets)):
            if intersection := set_i.intersect(sets[j]):
                candidates.append(intersection)

        # Calculate effective size and add contribution
        size = set_i.size() + subsets(set_i, -1, candidates)
        total += size * set_i.weight

    return total


PROGRAMS = parse_programs()

ans_part_1 = part1(PROGRAMS)
ans_part_2 = part2(PROGRAMS)

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 7477696999511
assert ans_part_2 == 3687727854171
