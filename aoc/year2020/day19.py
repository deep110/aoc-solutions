from aoc.utils import read_input

ms = read_input(2020, 19).split("\n")


def parse_rules():
    rules = {}
    for rule_str in ms:
        if rule_str == "":
            break
        key, val = rule_str.split(": ")
        key = int(key)
        if val.startswith('"'):
            rules[key] = val[1]
        else:
            options = []
            for r in val.split("|"):
                options.append(r.strip().split(" "))
            rules[key] = options

    return rules


RULES = parse_rules()


def part1():
    def build_regex_exp(rule_idx):
        rule = RULES[rule_idx]
        if isinstance(rule, str):
            return rule

        options = []
        for option in rule:
            option_exp = "".join(build_regex_exp(r) for r in option)
            options.append(option_exp)

        return "(" + "|".join(options) + ")"

    tc = 6
    print(RULES[tc])
    reg_exp = build_regex_exp(tc)
    print(RULES[tc], reg_exp)


def part2():
    pass


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

# assert ans_part_1 == 0
# assert ans_part_2 == 0
