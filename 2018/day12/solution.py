from os import path
import re


with open(path.join(path.dirname(__file__), "input.txt")) as f:
    a = f.readlines()


initial_state = "#......##...#.#.###.#.##..##.#.....##....#.#.##.##.#..#.##........####.###.###.##..#....#...###.##"
iters = 50000000000

def replace_str(old_str, new_str, si):
    return old_str[:si - 2] + new_str + old_str[si + 3:]


def evolve(curr_state):
    temp = curr_state[:2]
    for j in range(2, len(curr_state)-3):
        _pat = curr_state[j - 2:j + 3]
        if _pat in plant_list:
            temp += '#'
        else:
            temp += '.'

    return temp + curr_state[-3:]


def trim_start(state):
    i = 0
    for _y in state[:100]:
        if _y == '.':
            i += 1
        else:
            break

    return state[i:], i


def revive_end(state):
    c = 0
    for i in range(1, 201):
        if state[-i] == '.':
            c += 1
        else:
            break

    return state + "." * (200 - c)


def get_score(state, _pad):
    ans = 0
    for i, p in enumerate(state):
        if p == '#':
            ans += (i - _pad)
    return ans


p = re.compile(r"((\.|#){5}) => (\.|#)")
plant_list = []
non_plant_list = []

for i in a:
    _z = p.search(i)
    if _z.group(3) == '.':
        non_plant_list.append(_z.group(1))
    else:
        plant_list.append(_z.group(1))

padding = 200
pots = "." * padding + initial_state + "."*padding


cr = pots
for i in range(1001):
    cr = evolve(cr)

    # check for padding dots
    if i % 100 == 0:
        cr = revive_end(cr)
        cr, _p = trim_start(cr)
        padding -= _p
    # if i != 0 and (i % 1000 == 0):
    #     k.append(get_score(cr, padding))

base_score = get_score(cr, padding)

def calc(bs, li):
    return bs + 75000 * ((li/1000) -1)

print(base_score, calc(base_score, 3000))


def part1():
    pass

def part2():
    pass

print("Part1 solution: ", part1())
print("Part2 solution: ", part2())
