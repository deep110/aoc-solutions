"""
# Crab Combat

For part2, running naively takes around 700ms. But while browsing subreddit, i found this
[rust solution](https://github.com/maneatingape/advent-of-code-rust/blob/main/src/year2020/day22.rs)

The deterministic trick is an observation that if Player 1 holds the high card in a recursive
game, then they will always eventually win. This comes from the fact that all cards are unique,
so the highest card is always greater than the size of the remaining deck, so a further
recursive game will never trigger when this card is played in a round. This means that Player 1
will never lose this card, so will either win outright or by triggering the repetition rule.

This observation does not hold for Player 2. Although they can never lose the high card, they
could lose by the repetition rule, so the round needs to be played out in full.
"""

from collections import deque
from itertools import islice
from typing import Deque
from aoc.utils import read_input

MAX_ROUNDS = 700

ms = read_input(2020, 22).split("\n\n")
player1_deck = [int(i) for i in ms[0].split("\n")[1:]]
player2_deck = [int(i) for i in ms[1].split("\n")[1:]]


def get_score(deck):
    score = 0
    len_deck = len(deck)
    for i in range(len_deck):
        score += (len_deck - i) * deck[i]
    return score


def recursive_combat(deck1: Deque[int], deck2: Deque[int]):
    num_rounds = 0
    while len(deck1) > 0 and len(deck2) > 0:
        # Instead of caching tuples
        # Using u/mendelmunkis dirty trick to reduce runtime from 16ms to ~9ms
        #
        # Original code was:
        #
        # # See if this deck ordering is in cache
        # state = (tuple(deck1), tuple(deck2))
        # if state in cache:
        #     return True
        # cache.add(state)
        num_rounds += 1
        if num_rounds > MAX_ROUNDS:
            return True

        v1, v2 = deck1.popleft(), deck2.popleft()

        # we have to play recursive game
        if len(deck1) >= v1 and len(deck2) >= v2:
            sub_d1 = deque(islice(deck1, 0, v1))
            sub_d2 = deque(islice(deck2, 0, v2))

            # Player 1 always wins recursive games if they have the high card
            # this speeds up by a factor 50x
            if max(sub_d1) > max(sub_d2):
                is_p1_winner = True
            else:
                is_p1_winner = recursive_combat(sub_d1, sub_d2)
        else:
            is_p1_winner = v1 > v2

        if is_p1_winner:
            deck1.append(v1)
            deck1.append(v2)
        else:
            deck2.append(v2)
            deck2.append(v1)

    return len(deck1) > 0


def part1():
    p1_deck = deque(player1_deck)
    p2_deck = deque(player2_deck)

    while len(p1_deck) > 0 and len(p2_deck) > 0:
        a = p1_deck.popleft()
        b = p2_deck.popleft()
        if a > b:
            p1_deck.append(a)
            p1_deck.append(b)
        else:
            p2_deck.append(b)
            p2_deck.append(a)

    winning_deck = p1_deck if len(p1_deck) > 0 else p2_deck
    return get_score(winning_deck)


def part2():
    p1_deck = deque(player1_deck)
    p2_deck = deque(player2_deck)

    is_p1_winner = recursive_combat(p1_deck, p2_deck)
    winning_deck = p1_deck if is_p1_winner else p2_deck
    return get_score(winning_deck)


ans_part_1 = part1()
ans_part_2 = part2()

print("Part1 solution: ", ans_part_1)
print("Part2 solution: ", ans_part_2)

assert ans_part_1 == 32824
assert ans_part_2 == 36515
