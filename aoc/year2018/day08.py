from aoc.utils import read_input


def parse_input():
    ms = read_input(2018, 8).split(" ")
    return list(map(lambda x: int(x), ms))


def reduce_ln_cc(_ns):
    if len(_ns) > 0:
        ls = _ns.pop()
        _ns.append((ls[0] - 1, ls[1]))


def if_last_zero(_ns):
    if len(_ns) > 0:
        ls = _ns[-1]
        if ls[0] == 0:
            del _ns[-1]
            return True, ls[1]
        else:
            return False, ls[1]
    return False, 0


def get_next_chr(_i: str):
    return chr(ord(_i) + 1)


def part1(inp):
    nodes = []
    meta_data = 0

    i = 0
    while i < len(inp):
        # if last node has 0 child -> read meta data
        is_l0, val = if_last_zero(nodes)
        if is_l0:
            meta_data += sum(inp[i : i + val])
            i += val
        else:
            a, b = inp[i], inp[i + 1]
            i += 2
            # if there is last node, reduce its child count
            reduce_ln_cc(nodes)

            # if child no is 0 --> read all meta data entries
            if a == 0:
                meta_data += sum(inp[i : i + b])
                i += b
            else:
                nodes.append((a, b))

    return meta_data


def create_tree(inp):
    def __last_zero(_ns):
        if len(_ns) > 0:
            ls = _ns[-1]
            if ls[0] == 0:
                del _ns[-1]
                return True, ls[1], ls[2]
            else:
                return False, ls[1], ls[2]
        return False, 0, -1

    rel = {}
    curr_node_val = -1
    i = 0
    nodes = []
    while i < len(inp):
        # if last node has 0 child -> read meta data
        is_l0, val, ind = __last_zero(nodes)
        if is_l0:
            _p = rel[ind]
            rel[ind] = (_p[0], inp[i : i + val])
            i += val
        else:
            a, b = inp[i], inp[i + 1]
            i += 2
            # if there is last node, reduce its child count
            if len(nodes) > 0:
                ls = nodes.pop()
                nodes.append((ls[0] - 1, ls[1], ls[2]))
                parent = ls[2]
            else:
                parent = None
            if a == 0:
                sr = sum(inp[i : i + b])
                i += b
                curr_node_val += 1
                rel[curr_node_val] = (parent, sr)
            else:
                curr_node_val += 1
                rel[curr_node_val] = (parent, -1)
                nodes.append((a, b, curr_node_val))

    return rel


def part2(inp):
    inp = [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]

    def get_childs(index, tr):
        _p = []
        for i in tr:
            if tr[i][0] == index:
                _p.append(i)
        return _p

    _tree = create_tree(inp)
    print(_tree)

    def calc(ind, childs):
        print(ind, childs)

        for i in childs:
            if isinstance(_tree[i][1], list):
                return calc(i, get_childs(i, _tree))

    print(calc(0, get_childs(0, _tree)))


_input = parse_input()

print("Part1 solution: ", part1(_input))
print("Part2 solution: ", part2(_input))
