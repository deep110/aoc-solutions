import re

with open("input/input_4.txt") as f:
    ms = f.read().strip()

ms = ms.split("\n\n")
ms = list(map(lambda x: x.replace("\n", " "), ms))

HGT_PT = re.compile(r"(\d+)(in|cm)$")
HCL_PT = re.compile(r"#([0-9]|[a-f]){6}$")

def part1():
    valid = 0
    for i in ms:
        k = i.split(" ")
        is_cid = (len(k) == 7) and "cid" not in i
        if (len(k) == 8) or is_cid:
            valid += 1

    return valid


def is_valid_hgt(hgt):
    m = HGT_PT.search(hgt)
    if m:
        num = int(m[1])
        p = m[2]
        if p == "cm" and (num >= 150 and num <= 193):
            return True
        if p == "in" and (num >= 59 and num <= 76):
            return True

    return False 


def part2():
    valid = 0
    for i in ms:
        k = sorted(i.split(" "), key=lambda x: x[:2])
        is_cid = (len(k) == 7) and "cid" not in i
        is_valid = (len(k) == 8) or is_cid
        if is_valid:
            byr = int(k[0].split(":")[1])
            if not (byr >= 1920 and byr <= 2002):
                continue
            ecl = k[2 - is_cid].split(":")[1]
            if not ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                continue
            eyr = int(k[3 - is_cid].split(":")[1])
            if not (eyr >= 2020 and eyr <= 2030):
                continue
            hcl = k[4 - is_cid].split(":")[1]
            if not HCL_PT.search(hcl):
                continue
            hgt = k[5 - is_cid].split(":")[1]
            if not is_valid_hgt(hgt):
                continue            
            iyr = int(k[6 - is_cid].split(":")[1])
            if not (iyr >= 2010 and iyr <= 2020):
                continue
            pid = k[7 - is_cid].split(":")[1]
            if not (len(pid) == 9):
                continue

            valid += 1
    
    return valid

print("Part1 solution: ", part1())
print("Part2 solution: ", part2())
