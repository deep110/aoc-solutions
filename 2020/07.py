import re

with open("input/input_7.txt") as f:
    ms = f.readlines()

PAT = re.compile(r"(.*) bags contain (.*)")
BPAT = re.compile(r"(\d+) (.*) bags?")

ms = list(map(lambda x: x.strip(), ms))

tree = {}
reverse_tree = {}

def get_bag(x):
    m = BPAT.search(x.strip())
    if m:
        return (m[2], int(m[1]))
    else:
        return (None, 0)

for i in ms:
    m = PAT.search(i)
    a = m[1]
    b = list(map(lambda x: get_bag(x), m[2].split(",")))

    tree[a] = b
    for j in b:
        if j[0] not in reverse_tree:
            reverse_tree[j[0]] = [a]
        else:
            reverse_tree[j[0]].append(a)

def part1():
    bags_sg = reverse_tree["shiny gold"]
    all_bgs = []
    while len(bags_sg) > 0:
        p = bags_sg[0]
        all_bgs.append(p)
        if p in reverse_tree:
            bags_sg.extend(reverse_tree[p])
        del bags_sg[0]

    return len(set(all_bgs))


def part2(bag_name="shiny gold"):
    bags = tree[bag_name]
    if len(bags) == 1 and bags[0][0] is None:
            return 0
    
    k = 0
    for i in bags:
        bn, c = i
        k += c + c * part2(bn)

    return k
        
print("Part1 solution: ", part1())
print("Part2 solution: ", part2())
