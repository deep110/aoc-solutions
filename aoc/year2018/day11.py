"""
# Chronal Charge

Building a [summed-area table](https://en.wikipedia.org/wiki/Summed-area_table) allows us
to compute the power of any rectangle with only 4 array lookups.
This is really nice idea, using exclusion, inclusion principle of set theory. At least that is
how I understood it.

For Part2, instead of searching all sizes, I used a binary search to get to the solution faster.
"""


def create_power_grid(grid_serial=7400):
    # Pre-calculate the summed area table
    grid = [[0] * 301 for _ in range(301)]

    for y in range(1, 301):
        row_sum = 0
        for x in range(1, 301):
            # Calculate power level
            rid = x + 10
            power = ((rid * y + grid_serial) * rid) // 100 % 10 - 5

            # Add to running sum for this row
            row_sum += power

            # Calculate summed area value
            grid[y][x] = row_sum + grid[y - 1][x]

    return grid


def get_area_sum(grid, x1, y1, size):
    x2, y2 = x1 + size - 1, y1 + size - 1
    return grid[y2][x2] - grid[y2][x1 - 1] - grid[y1 - 1][x2] + grid[y1 - 1][x1 - 1]


def find_largest(grid, size):
    max_power = float("-inf")
    best_x = best_y = 0

    for y in range(1, 302 - size):
        for x in range(1, 302 - size):
            power = get_area_sum(grid, x, y, size)
            if power > max_power:
                max_power = power
                best_x, best_y = x, y

    return max_power, best_x, best_y


def part1(grid):
    _, x, y = find_largest(grid, 3)
    return f"{x},{y}"


def part2(grid):
    # Use binary search to find optimal size
    left, right = 1, 300
    max_power = float("-inf")
    result = None
    best_size = None

    while right - left > 3:
        mid = (left + right) // 2

        # Check both mid and mid+1 to determine direction
        power1, x1, y1 = find_largest(grid, mid)
        power2, x2, y2 = find_largest(grid, mid + 1)

        if power1 > max_power:
            max_power = power1
            result = (x1, y1, mid)
            best_size = mid
        if power2 > max_power:
            max_power = power2
            result = (x2, y2, mid + 1)
            best_size = mid + 1

        if power1 > power2:
            right = mid
        else:
            left = mid

    # Only fine-tune one size up and down from our best result
    for size in [best_size - 1, best_size + 1]:
        if 1 <= size <= 300:  # Stay in bounds
            power, x, y = find_largest(grid, size)
            if power > max_power:
                max_power = power
                result = (x, y, size)

    return f"{result[0]},{result[1]},{result[2]}"


# Run solution
grid = create_power_grid()
ans_part_1 = part1(grid)
ans_part_2 = part2(grid)

print("Part1 solution:", ans_part_1)
print("Part2 solution:", ans_part_2)

assert ans_part_1 == "34,72"
assert ans_part_2 == "233,187,13"
