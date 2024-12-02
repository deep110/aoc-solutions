import math


def get_nearest_odd_sq(target):
    n = 3
    while target - n * n >= 0:
        n += 2
    return n - 2


def part1():
    """
    Spiral Memory
    37 36  35  34  33  32 31
    38 17  16  15  14  13 30
       18   5   4   3  12 29
       19   6   1   2  11 28
       20   7   8   9  10 27
       21  22  23   24 25 26

    1. Fill the grid, and find the position
    2. [Optimization]
    Since bottom corner are odd squares (1, 9, 25, 49, ...), find the nearest odd square less than target
    and fill
    """
    target = 361527

    n = get_nearest_odd_sq(target)
    # this n is also the arm length, i.e that many numbers will be on that arm
    n_index = math.trunc(n / 2)

    # initialize the target index, considering (0, 0) as start
    target_index = [n_index, -n_index]
    diff = target - n * n

    # now walk
    walk_dir = 0
    while diff > 0:
        # walk 1 right
        if walk_dir == 0:
            target_index[0] += 1
            diff -= 1
            walk_dir += 1
        elif walk_dir == 1:
            # n+1 up
            target_index[1] += min(diff, n)
            diff -= min(diff, n)
            walk_dir += 1
        elif walk_dir == 2:
            target_index[0] -= min(diff, n+1)
            diff -= min(diff, n+1)
            walk_dir += 1
        elif walk_dir == 3:
            target_index[1] -= min(diff, n+1)
            diff -= min(diff, n+1)
            walk_dir += 1
        else:
            target_index[0] += min(diff, n+1)
            diff -= min(diff, n+1)
            walk_dir == 0

    return abs(target_index[0]) + abs(target_index[1])

def part2():
    pass


print("Part1 solution: ", part1())
print("Part2 solution: ", part2())
