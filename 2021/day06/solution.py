from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

counters = list(map(lambda x: int(x), ms[0].strip().split(",")))

def simulate(_fc_dict):
    zero_num = _fc_dict[0]

    for c in range(8):
        _fc_dict[c] = _fc_dict[c + 1]
    
    _fc_dict[6] += zero_num
    _fc_dict[8] = zero_num


def get_total_fishes(_fish_counter, num_days):
    fc_dict = {}
    for i in range(9):
        fc_dict[i] = 0

    for i in counters:
        fc_dict[i] += 1

    for d in range(num_days):
        simulate(fc_dict)

    total_fishes = 0
    for i in range(9):
        total_fishes += fc_dict[i]
    
    return total_fishes

def part1():
    return get_total_fishes(counters, 80)

def part2():
    return get_total_fishes(counters, 256)

print("Part1 solution: ", part1())
print("Part2 solution: ", part2())
