from itertools import *

def f(x, y, z, w):
    return (not (x <= z)) or (y == w) or y

for t in product([0, 1], repeat=7):
    tab = [(1, 0, t[0], t[1]),
           (t[2], 1, 0, t[3]),
           (0, t[4], t[5], t[6])]
    if set(tab).__len__() != 3: continue
    for p in permutations("xyzw"):
        if [f(**dict(zip(p, row))) for row in tab] == [0, 0, 0]:
            print(p)