"""
# Combo Breaker

The card loop size is found using the
[Baby-step giant-step algorithm](https://en.wikipedia.org/wiki/Baby-step_giant-step). This takes
only √20201227 = 4495 steps, compared to potentially up to 20201227 steps for the brute force approach.
This reduced the runtime from 240ms to ~0.8ms

The method described to calculate encryption key is called [modular exponentiation](https://en.wikipedia.org/wiki/Modular_exponentiation).
There are multiple ways to calculate it, one way is described in the problem. It takes around ~160ms
to calculate in first way. There is more efficient approach. We can use Right-to-left binary method
which uses [exponentiation by squaring](https://en.wikipedia.org/wiki/Exponentiation_by_squaring). This
reduces the runtime to 0.26 ms.
"""

import math
from typing import Dict
from aoc.utils import read_input

ms = read_input(2020, 25).split("\n")
CARD_PUBLIC_KEY = int(ms[0])
DOOR_PUBLIC_KEY = int(ms[1])
PRIME_KEY = 20201227


def baby_step_giant_step(subject: int, public_key: int, mod: int) -> int:
    """
    Find x such that (subject^x) % mod = public_key using baby-step giant-step algorithm
    """
    # Calculate m = ceil(sqrt(n))
    m = math.ceil(math.sqrt(mod - 1))

    # Baby-step: Calculate and store baby_steps[subject^j % mod] = j for j in [0, m)
    baby_steps: Dict[int, int] = {}
    value = 1
    for j in range(m):
        baby_steps[value] = j
        value = (value * subject) % mod

    # Calculate factor = subject^(-m) % mod
    #
    # We can calculate the multiplicative inverse from Fermat's Little Theorem:
    # Multiplicative Inverse of a:  1/a  =  a^(n-2)  (mod n)
    factor = pow(subject, m * (mod - 2), mod)

    # Giant-step: Check if giant * (baby_step) = public_key
    value = public_key
    for i in range(m):
        if value in baby_steps:
            return i * m + baby_steps[value]
        value = (value * factor) % mod


def modular_exponentiation(base: int, exponent: int, modulus: int):
    result = 1
    base = base % modulus
    while exponent > 0:
        # if exponent is odd
        if exponent & 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent >>= 1
    return result


def part1():
    loop_number = baby_step_giant_step(7, CARD_PUBLIC_KEY, PRIME_KEY)

    # We calculate encryption key using fast modular exponentiation
    return modular_exponentiation(DOOR_PUBLIC_KEY, loop_number, PRIME_KEY)


ans_part_1 = part1()

print("Part1 solution: ", ans_part_1)

assert ans_part_1 == 16457981
