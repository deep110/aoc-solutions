from os import path

with open(path.join(path.dirname(__file__), "input.txt")) as f:
    ms = f.readlines()

class Bingo(object):
    def __init__(self, _numbers):
        self.data = []
        for i in _numbers:
            arr = list(filter(lambda x: len(x) > 0, i.strip().split(" ")))
            self.data.extend(arr)

        self.mark = [0] * len(self.data)

    def put(self, num):
        if num in self.data:
            self.mark[self.data.index(num)] = 1

    def reset(self):
        self.mark = [0] * len(self.data)
    
    def is_win(self):
        # check rows
        for i in range(0, len(self.data), 5):
            if sum(self.mark[i:i+5]) == 5:
                return True
        
        # check columns
        for i in range(0, 5):
            _sum = 0
            for j in range(0, 5):
                _sum += self.mark[i+ j*5]
            if _sum == 5:
                return True

        return False

    def unmarked_sum(self):
        unmarked_sum = 0
        for e, m in enumerate(self.mark):
            if m == 0:
                unmarked_sum += int(self.data[e])
        return unmarked_sum


# parse lot
draws = ms[0].strip().split(",")
cards = []

# parse bingo cards
for i in range(1, len(ms), 6):
    cards.append(Bingo(ms[i+1: i+6]))


def part1():
    winning_card = None
    winning_lot = -1
    for i in draws:
        for c in cards:
            c.put(i)
            if c.is_win():
                winning_card = c
                break
        if winning_card is not None:
            winning_lot = int(i)
            break

    return winning_card.unmarked_sum() * winning_lot
    

def part2():
    last_card = None
    winning_lot = -1
    rem_cards = cards.copy()
    for c in rem_cards:
        c.reset()

    for i in draws:
        j = 0
        while j < len(rem_cards):
            c = rem_cards[j]
            c.put(i)

            if c.is_win():
                if len(rem_cards) == 1:
                    last_card = c
                    winning_lot = int(i)
                    break
                else:
                    rem_cards.pop(j)
            else:
                j += 1

            
        if last_card is not None:
            break
    
    return last_card.unmarked_sum() * winning_lot

print("Part1 solution: ", part1())
print("Part2 solution: ", part2())
