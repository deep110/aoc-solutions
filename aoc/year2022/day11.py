import re
from aoc.utils import read_input

ms = read_input(2022, 11).split("\n\n")

ITEM_PATTERN = re.compile(r"Starting items: (.*)")
OP_PATTERN = re.compile(r"Operation: new = old (\+|\*) (old|\d+)")
TEST_PATTERN = re.compile(r"divisible by (\d+)")
THROW_PATTERN = re.compile(r"If (true|false): throw to monkey (\d+)")


class Monkey(object):
    def __init__(self, index, _input):
        self.index = index
        self.items = []
        self.op = None
        self.divide_by = 1
        self.throw = {True: -1, False: -1}
        self.total_inspects = 0

        self.parse(_input)

    def parse(self, _input: str):
        p = _input.split("\n")

        # parse items
        its = eval(ITEM_PATTERN.search(p[1])[1], {}, {})
        if isinstance(its, int):
            its = [its]
        self.items = list(its)

        # parse op
        ops = OP_PATTERN.search(p[2])
        self.op2 = {"op": ops[1], "num": ops[2]}
        if ops[2] != "old":
            self.op2["num"] = int(ops[2])

        # parse divide
        self.divide_by = int(TEST_PATTERN.search(p[3])[1])
        self.throw[True] = int(THROW_PATTERN.search(p[4])[2])
        self.throw[False] = int(THROW_PATTERN.search(p[5])[2])

    def inspect(self, worry_reduce):
        it = self.items.pop(0)
        if self.op2["num"] == "old":
            it = it * it
        else:
            if self.op2["op"] == "*":
                it *= self.op2["num"]
            elif self.op2["op"] == "+":
                it += self.op2["num"]

        it = worry_reduce(it)

        is_divisible = (it % self.divide_by) == 0
        self.total_inspects += 1

        return it, self.throw[is_divisible]

    def __repr__(self):
        return f"Monkey {self.index}: {self.total_inspects}"


def part1():
    NUM_ROUNDS = 20
    monkeys = [Monkey(i, x) for i, x in enumerate(ms)]

    for r in range(NUM_ROUNDS):
        for m in monkeys:
            while len(m.items) > 0:
                wl, new_m_index = m.inspect(lambda x: int(x / 3))
                monkeys[new_m_index].items.append(wl)

    monkeys.sort(key=lambda x: x.total_inspects, reverse=True)
    return monkeys[0].total_inspects * monkeys[1].total_inspects


def part2():
    NUM_ROUNDS = 10000
    monkeys = [Monkey(i, x) for i, x in enumerate(ms)]
    total_prod = 1
    for m in monkeys:
        total_prod *= m.divide_by

    for r in range(NUM_ROUNDS):
        for m in monkeys:
            while len(m.items) > 0:
                wl, new_m_index = m.inspect(lambda x: x % total_prod)
                monkeys[new_m_index].items.append(wl)

    monkeys.sort(key=lambda x: x.total_inspects, reverse=True)
    return monkeys[0].total_inspects * monkeys[1].total_inspects


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 102399
assert ans_part_2 == 23641658401
