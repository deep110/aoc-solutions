from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

ms = list(map(lambda x: x.strip(), ms))


def row(code):
    x, y = (0, 127)
    for i in code:
        if i == "F":
            (x, y) = (x, x + (y - x) // 2)
        else:
            (x, y) = (x + (y - x) // 2 + 1, y)

    return x


def column(code):
    x, y = (0, 7)
    for i in code:
        if i == "L":
            (x, y) = (x, x + (y - x) // 2)
        else:
            (x, y) = (x + (y - x) // 2 + 1, y)
    return x


def seat_id(_id):
    # first 7 letters tells row, last 7 tells column
    r = row(_id[:7])
    c = column(_id[7:])
    return r * 8 + c, r, c


def part12():
    max_sid = -1
    seats = [None] * 128
    for i in ms:
        s_id, r, c = seat_id(i)
        if s_id > max_sid:
            max_sid = s_id

        if seats[r]:
            seats[r].append((r, c))
        else:
            seats[r] = [(r, c)]

    # for part2
    our_row, our_col = (None, None)
    for row in seats:
        if row and len(row) == 7:
            # this row contains our missing seat
            sorted_row = sorted(row)
            idx = 0
            for r, c in sorted_row:
                if idx == c:
                    idx += 1
                else:
                    our_row, our_col = r, idx
                    break

    return max_sid, our_row * 8 + our_col


ans_part_1, ans_part_2 = part12()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 832
assert ans_part_2 == 517
