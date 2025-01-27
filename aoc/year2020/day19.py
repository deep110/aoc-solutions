"""
# Monster Messages

## Part1

I am doing a recursive matching of string on rules, instead of precomputing the rule options.

## Part2

Rule 8 (42 | 42 8) means:

- Match rule 42 once OR
- Match rule 42 followed by rule 8 again. This effectively means "match rule 42
one or more times" (like regex 42+)

Rule 11 (42 31 | 42 11 31) means:

- Match rule 42 followed by rule 31 OR
- Match rule 42, then rule 11, then rule 31
- This creates pairs of 42s and 31s, like: 42 31 or 42 42 31 31 or 42 42 42 31 31 31

Rule 0 (8 11) combines these, meaning a valid message must have:

Some number of rule 42 matches (from rule 8)
Followed by some pairs of 42 and 31 (from rule 11). This means there must be MORE matches of
rule 42 than rule 31 then only message is valid.

"""

from aoc.utils import read_input

ms = read_input(2020, 19).split("\n")
rules_end_idx = ms.index("")


def parse_rules():
    rules = [None] * 150
    for rule_str in ms[:rules_end_idx]:
        key, val = rule_str.split(": ")
        rule_num = int(key)
        if val.startswith('"'):
            rules[rule_num] = val[1]
        else:
            options = []
            for r in val.split(" | "):
                options.append([int(x) for x in r.split()])
            rules[rule_num] = options
    return rules


def check_rule(message, rule_idx, message_idx):
    if message_idx >= len(message):
        return None

    rule = rules[rule_idx]

    # case when a letter is found
    if isinstance(rule, str):
        # we are checking a part of message and rule should match the message
        if message_idx < len(message) and message[message_idx] == rule:
            return message_idx + 1
        return None

    for option in rule:
        current_idx = message_idx
        matches = True

        for subrule in option:
            result = check_rule(message, subrule, current_idx)
            if result is None:
                matches = False
                break
            current_idx = result
        if matches:
            return current_idx

    return None


def part1():
    count = 0
    for i in range(rules_end_idx + 1, len(ms)):
        message = ms[i]
        if check_rule(message, 0, 0) == len(message):
            count += 1

    return count


def part2():
    count = 0
    for i in range(rules_end_idx + 1, len(ms)):
        message = ms[i]
        # rule 0: 8 11
        # this translates to arbitrary number of 42s followed by 31s
        # for our message to be valid, we need at least two 42 and one 31

        count_42 = 0
        count_31 = 0
        message_idx = 0

        # count 42s
        while True:
            result = check_rule(message, 42, message_idx)
            if result is None:
                break
            else:
                message_idx = result
                count_42 += 1

        if count_42 < 2 or message_idx == len(message):
            continue

        # count 31s
        while True:
            result = check_rule(message, 31, message_idx)
            if result is None:
                break
            else:
                message_idx = result
                count_31 += 1

        if count_31 >= 1 and count_42 > count_31 and message_idx == len(message):
            count += 1

    return count


rules = parse_rules()

ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 233
assert ans_part_2 == 396
