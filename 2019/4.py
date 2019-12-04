from collections import Counter

_range = (372304, 847060)

def is_increase(a):
    q = -1
    for i in a:
        t = int(i)
        if t < q:
            return False
        q = t
    
    return True

def is_double(a):
    if len(set(a)) < len(a):
        c = dict(Counter(a)).values()
        if 2 in list(c):
            return True

    return False

p = 0
for i in range(_range[0], _range[1]+1):
    a = list(str(i))
    if is_increase(a) and is_double(a):
        p += 1

print(p)
