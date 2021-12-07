from os import path
import math

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

positions = list(map(lambda x: int(x), ms[0].strip().split(",")))
_min = min(positions)
_max = max(positions)

def fuel_expenditure(_positions, target_pos, func):
    fuel = 0
    for i in _positions:
        fuel += func(i - target_pos)
    
    return fuel

def new_exp(val):
    val = abs(val)
    return int(val * (val +1) / 2)


def part1():
    _min = min(positions)
    _max = max(positions)

    least_fuel = math.inf
    for i in range(_min, _max+1):
        f = fuel_expenditure(positions, i, abs)
        if f < least_fuel:
            least_fuel = f
    
    return least_fuel

def part2():
    least_fuel = math.inf
    for i in range(_min, _max+1):
        f = fuel_expenditure(positions, i, new_exp)
        if f < least_fuel:
            least_fuel = f

    return least_fuel

print("Part1 solution: ", part1())
print("Part2 solution: ", part2())
