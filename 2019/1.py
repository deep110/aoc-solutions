with open("input/input_1.txt") as f:
    ms = f.readlines()

ms = list(map(lambda x: int(x.strip()), ms))


def part1():
    fuels_req = list(map(lambda x: int(x/3) - 2, ms))
    print(sum(fuels_req))


def part2():

    def calc_total_fr(mass: int):
        t = 0
        while mass > 3:
            fr = int(mass/3) - 2
            if fr > 0:
                t += fr
            mass = fr
        return t

    fuels_req = list(map(lambda x: calc_total_fr(x), ms))
    print(sum(fuels_req))


part2()