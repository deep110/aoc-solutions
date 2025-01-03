from os import path
import re
from typing import List

FIELD_PATTERN = re.compile(r"(.*): (\d+)\-(\d+) or (\d+)\-(\d+)")

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

break_idx = ms.index("\n")
our_ticket_idx = break_idx + 2
nearby_tickets_idx = our_ticket_idx + 3


def parse_fields():
    fields = {}
    for field_str in ms[:break_idx]:
        g = FIELD_PATTERN.match(field_str).groups()
        fields[g[0]] = (int(g[1]), int(g[2]), int(g[3]), int(g[4]))

    return fields


FIELDS = parse_fields()
OUR_TICKET = list(map(lambda x: int(x), ms[our_ticket_idx].strip().split(",")))
NEAR_BY_TICKETS = list(
    [int(item) for item in sublist]
    for sublist in map(lambda x: x.strip().split(","), ms[nearby_tickets_idx:])
)


def part1():
    def is_invalid(n: int):
        for a, b, c, d in FIELDS.values():
            if (n >= a and n <= b) or (n >= c and n <= d):
                return False
        return True

    valid_tickets = []
    invalid_count = 0
    for ticket in NEAR_BY_TICKETS:
        valid = True
        for num in ticket:
            if is_invalid(num):
                invalid_count += num
                valid = False
        if valid:
            valid_tickets.append(ticket)

    return invalid_count, valid_tickets


def part2(valid_tickets: List[List[int]]):
    len_ticket = len(OUR_TICKET)
    valid_field_positions = {}
    product = 1

    # first iterate over every field and find which positions fulfill the criteria
    for field in FIELDS:
        a, b, c, d = FIELDS[field]
        valid_positions = set()

        for pos in range(len_ticket):
            is_valid = True
            for ticket in valid_tickets:
                num = ticket[pos]
                if (num < a or num > b) and (num < c or num > d):
                    is_valid = False
                    break

            if is_valid:
                valid_positions.add(pos)

        valid_field_positions[field] = valid_positions

    # next eliminate the positions
    removed_set = set()
    for field, valid_pos in sorted(
        valid_field_positions.items(), key=lambda x: len(x[1])
    ):
        final_pos = list(valid_pos - removed_set)[0]
        removed_set.add(final_pos)

        if field.startswith("departure"):
            product *= OUR_TICKET[final_pos]

    return product


ans_part_1, valid_tickets = part1()
ans_part_2 = part2(valid_tickets)

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 19093
assert ans_part_2 == 5311123569883
