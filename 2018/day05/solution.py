from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    a = f.read()

a = a.replace('\n', '')

def is_match(s1, s2):
    return (abs(ord(s1) - ord(s2))) == 32

def part1(a):
    l = None
    k = ''
    while True:
        for c, i in enumerate(a):
            if l:
                if not is_match(l, i):
                    k = k + l
                    l = i
                else:
                    l = None
            else:
                l = i
            if c == (len(a) - 1) and (l is not None):
                k += i
        if len(a) == len(k):
            break
        else:
            a = k
            k = ''
            l = None

    return len(k)

def part2(a):
    l = 100000
    for i in range(97, 123):
        p = a.replace(chr(i), "")
        p = p.replace(chr(i-32), "")
        v = part_one(p)
        if v < l:
            l = v

        print('completed', i)
    return l


print("Part1 solution: ", part1(a))
print("Part2 solution: ", part2(a))
