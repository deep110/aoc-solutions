with open("input/input_5.txt") as f:
    ms = f.readlines()

ms = list(map(lambda x: x.strip(), ms))

def row(code):
    x, y = (0, 127)
    for i in code:
        if i == "F":
            (x, y) = (x, x + (y-x)//2)
        else:
            (x, y) = (x + (y-x)//2 + 1,y)

    return x

def column(code):
    x, y = (0, 7)
    for i in code:
        if i == "L":
            (x, y) = (x, x + (y-x)//2)
        else:
            (x, y) = (x + (y-x)//2 + 1,y)
    return x

def seat_id(_id):
    r = row(_id[:7])
    c = column(_id[7:])
    return r * 8 + c , r, c

def part1():
    p = []
    for i in ms:
        k, _, _ = seat_id(i)
        p.append(k)

    return max(p)


def part2():
    rs = [None] * 110
    for i in ms:
        k, r, c = seat_id(i)
        if rs[r]:
            rs[r].append((r, c))
        else:
            rs[r] = [(r, c)]
    
    for i in rs:
        if i and len(i) < 8:
            print(i)

    return 64*8+5

print("Part1 solution: ", part1())
print("Part2 solution: ", part2())

    