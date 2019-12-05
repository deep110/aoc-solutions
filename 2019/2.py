with open("input/input_2.txt") as f:
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
    ans = run_program(arr, 12, 2)
    print(ans)


def part2():
    final_out = 19690720
    for i in range(20, 40):
        b = arr[:]
        ans = run_program(b, 77, 2+i)
        if ans == final_out:
            print("out is", 77*100+(2+i))

part2()
