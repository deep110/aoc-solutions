from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

ms = list(map(lambda x: x.strip(), ms))

def get_rating(is_reversed=False):
    code_len = int(len(ms[0]))
    valid_codes = ms.copy()

    for i in range(code_len):
        if len(valid_codes) == 1:
            break

        columns = list(zip(*valid_codes))
        column_to_check = columns[i]
        key_number = "0"

        if is_reversed:
            if column_to_check.count("0") > column_to_check.count("1"):
                key_number = "1"
        else:
            if column_to_check.count("1") >= column_to_check.count("0"):
                key_number = "1"
        
        remaining_codes = []
        for number in valid_codes:
            if number[i] == key_number:
                remaining_codes.append(number)
        valid_codes = remaining_codes

    return valid_codes[0]


def part1():
    columns = zip(*ms)
    gamma = ""
    epsilon = ""

    for column in columns:
        if column.count("1") > column.count("0"):
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    return int(gamma, 2) * int(epsilon, 2)


def part2():
    oxygen_gen = get_rating()
    co2_scrub = get_rating(True)

    return int(oxygen_gen, 2) * int(co2_scrub, 2)


print("Part1 solution: ", part1())
print("Part2 solution: ", part2())
