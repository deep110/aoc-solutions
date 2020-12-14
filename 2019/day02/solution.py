from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    arr = f.read()

arr = arr.split(",")
arr = list(map(lambda x: int(x), arr))

def run_program(cs, noun, verb):
    cs[1] = noun
    cs[2] = verb
    for i in range(0, len(cs), 4):
        if cs[i] == 99:
            break
        if cs[i] == 1:
            cs[cs[i+3]] = cs[cs[i+1]] + cs[cs[i+2]]
        if cs[i] == 2:
            cs[cs[i+3]] = cs[cs[i+1]] * cs[cs[i+2]]

    return cs[0]

def part1():
    return run_program(arr, 12, 2)


def part2():
    final_out = 19690720
    for i in range(20, 40):
        b = arr[:]
        ans = run_program(b, 77, 2+i)
        if ans == final_out:
            return 77*100+(2+i)

print("Part1 solution: ", part1())
print("Part2 solution: ", part2())
