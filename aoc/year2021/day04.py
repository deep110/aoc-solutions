"""
# Day 4: Giant Squid

Instead of simulating the bingo game turn by turn, we can pre-calculate when each board will
win by looking at its rows and columns.

Steps in this trick:
1. Map each number in every bingo board to its turn number.
2. The MAXIMUM turn in that row/column tells you when that complete line would be marked,
because all numbers in a line needs to be called before it wins.
3. The MINIMUM of these maximums tells you when the board wins.
4. The MINIMUM of every board turn win will tell which board wins first

For Part2,
The MAXIMUM of every board turn win will tell which board will win last.
"""

from typing import Dict
from aoc.utils import read_input

ms = read_input(2021, 4).split("\n\n")


class BingoCard:
    def __init__(self, numbers_str: str):
        self.data = [-1] * 25
        k = 0
        for i in numbers_str.split("\n"):
            for j in i.split(" "):
                if j != "":
                    self.data[k] = int(j)
                    k += 1

    def fill_winning_turn(self, turn_map: Dict[int, int]):
        self.turn_data = [-1] * 25
        for i in range(25):
            self.turn_data[i] = turn_map[self.data[i]]

        self.winning_turn = 10000000

        # get for rows
        for i in range(0, 25, 5):
            max_turn = max(self.turn_data[i : i + 5])
            if max_turn < self.winning_turn:
                self.winning_turn = max_turn

        # get for columns
        for i in range(0, 5):
            max_turn = 0
            for j in range(0, 5):
                if self.turn_data[i + j * 5] > max_turn:
                    max_turn = self.turn_data[i + j * 5]

            if max_turn < self.winning_turn:
                self.winning_turn = max_turn

    def unmarked_sum(self):
        unmarked_sum = 0
        for i in range(25):
            if self.turn_data[i] > self.winning_turn:
                unmarked_sum += self.data[i]

        return unmarked_sum


# parse lot and bingo cards
draws = list(map(lambda x: int(x), ms[0].split(",")))
cards = [BingoCard(ms[i]) for i in range(1, len(ms))]


def part12():
    turn_map = {}
    for i in range(len(draws)):
        turn_map[draws[i]] = i

    cards[0].fill_winning_turn(turn_map)

    first_win_card: BingoCard = cards[0]
    last_win_card: BingoCard = cards[0]

    for i in range(1, len(cards)):
        bingo_card = cards[i]
        bingo_card.fill_winning_turn(turn_map)
        if bingo_card.winning_turn < first_win_card.winning_turn:
            first_win_card = bingo_card

        if bingo_card.winning_turn > last_win_card.winning_turn:
            last_win_card = bingo_card

    ans_p1 = draws[first_win_card.winning_turn] * first_win_card.unmarked_sum()
    ans_p2 = draws[last_win_card.winning_turn] * last_win_card.unmarked_sum()

    return ans_p1, ans_p2


ans_part_1, ans_part_2 = part12()

print("Part1 solution:", ans_part_1)
print("Part2 solution:", ans_part_2)

assert ans_part_1 == 11774
assert ans_part_2 == 4495
