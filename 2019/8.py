from collections import Counter
import numpy as np

with open("input/input_8.txt") as f:
    ins = f.read().strip()

(w, h) = (25, 6)
layer_len = h * w
d = int(len(ins)/layer_len)

def part1():
    layers = []

    for i in range(0, len(ins), layer_len):
        layer = ins[i:i+layer_len]
        layers.append(layer)

    def min_f(x):
        c = Counter(list(x))
        return c['0']

    req_layer = min(layers, key=min_f)

    c = Counter(list(req_layer))
    return c['1'] * c['2']

def part2():
    def get_px(x):
        for i in x:
            if i != 2:
                return i
        return 2

    arr = np.array(list(ins), dtype=np.int8)
    layers = arr.reshape((d, layer_len))

    final_img = []
    for i in range(0, layer_len):
        final_img.append(get_px(layers[:, i]))

    final_img = np.array(final_img, dtype=np.int8)
    final_img = final_img.reshape((h, w))
    print(final_img) # lgyhb


part1()
part2()