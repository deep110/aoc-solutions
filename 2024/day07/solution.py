from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

eqns = []
for m in ms:
    a = m.split(":")
    rhs = a[1].strip().split(" ")
    rhs = list(map(lambda x: int(x), rhs))
    eqns.append([int(a[0]), rhs])


def evaluate(result, curr_index, eqn, is_part2=False):
    if curr_index == 0:
        return result == eqn[0]

    if evaluate(result - eqn[curr_index], curr_index - 1, eqn, is_part2):
        return True

    if result % eqn[curr_index] == 0 and evaluate(
        result // eqn[curr_index], curr_index - 1, eqn, is_part2
    ):
        return True

    if is_part2:
        result_str = str(result)
        len_op = len(str(eqn[curr_index]))

        if len(result_str) > len_op and result_str[-1 * len_op :] == str(
            eqn[curr_index]
        ):
            if evaluate(
                int(result_str[: len(result_str) - len_op]),
                curr_index - 1,
                eqn,
                is_part2,
            ):
                return True

    return False


correct_eqns = []


def part1():
    total_calib = 0

    for i in range(len(eqns)):
        eqn = eqns[i]
        is_valid = evaluate(eqn[0], len(eqn[1]) - 1, eqn[1])
        if is_valid:
            correct_eqns.append(i)
            total_calib += eqn[0]

    return total_calib


def part2():
    total_calib = 0

    for i in range(len(eqns)):
        eqn = eqns[i]
        if i in correct_eqns:
            total_calib += eqn[0]
        elif evaluate(eqn[0], len(eqn[1]) - 1, eqn[1], is_part2=True):
            total_calib += eqn[0]

    return total_calib


ans_part_1 = part1()
ans_part_2 = part2()

assert ans_part_1 == 303766880536
assert ans_part_2 == 337041851384440

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)
