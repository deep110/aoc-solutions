"""
# Operation Order

Part1 was very straight forward, even to do without any string manipulations or using python eval.

For Part2, i had to read up a bit on how algorithmic expressions are evaluated. Came across
[Shunting Yard Algorithm](https://mathcenter.oxford.emory.edu/site/cs171/shuntingYardAlgorithm/).
This converts infix notation to postfix or reverse Polish notation (RPN). Then we just solve the RPN stack.
"""
from aoc.utils import read_input

SPACES = [" ", "\n"]
OPS = ["+", "*"]

expressions = read_input(2020, 18).split("\n")


def evaluate_rpn(postfix_expr):
    stack = []
    for char in postfix_expr:
        if char in OPS:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == "+":
                result = operand1 + operand2
            else:
                result = operand1 * operand2
            stack.append(result)
        else:
            stack.append(char)

    return stack[-1]


def part1():
    # using op stack and num stack like in shunting yard algo
    # though instead of converting to postfix or RPN, we can directly eval
    total_sum = 0
    for expression in expressions:
        op_stack = ["+"]
        num_stack = [0]
        for c in expression:
            if c in SPACES:
                continue
            elif c in OPS:
                op_stack[-1] = c
            elif c == "(":
                op_stack.append("+")
                num_stack.append(0)
            elif c == ")":
                op_stack.pop()
                res = num_stack.pop()
                if op_stack[-1] == "+":
                    num_stack[-1] += res
                else:
                    num_stack[-1] *= res
            else:
                if op_stack[-1] == "+":
                    num_stack[-1] += int(c)
                else:
                    num_stack[-1] *= int(c)

        total_sum += num_stack[-1]
    return total_sum


def part2():
    # here precedence order of add and multiply is changed.
    # We will use Shunting Yard Algorithm
    total_sum = 0
    precedence = {"+": 2, "*": 1}

    for expression in expressions:
        operator_stack = []
        rpn_stack = []

        # First create a RPN notation stack
        for token in expression:
            if token in SPACES:
                continue
            elif token in OPS:
                while (
                    operator_stack
                    and operator_stack[-1] != "("
                    and precedence[token] <= precedence[operator_stack[-1]]
                ):
                    rpn_stack.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == "(":
                operator_stack.append(token)
            elif token == ")":
                while operator_stack[-1] != "(":
                    rpn_stack.append(operator_stack.pop())
                operator_stack.pop()  # Remove '('
            else:
                rpn_stack.append(int(token))

        while operator_stack:
            rpn_stack.append(operator_stack.pop())

        # now solve it
        total_sum += evaluate_rpn(rpn_stack)

    return total_sum


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 209335026987
assert ans_part_2 == 33331817392479
