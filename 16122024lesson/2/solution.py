from itertools import *

def f1(x,y,z,w):
    return (x or not y) <= (w==z)
def f2(x,y,z,w):
    return (x or not y) == (w<=z)

for i in product((0,1), repeat=6):
    tab = [(0, i[0], 0, 0),
           (i[1], 1, 1, i[2]),
           (i[4], 0, 0, 0)]
    res = [(0, 0),
           (0, i[3]),
           (i[5], 0)]
    if {tab[0] + res[0], tab[1] + res[1], tab[2] + res[2]}.__len__() != 3: continue
    for p in permutations("xyzw"):
        for k in range(3):
            if (f1(**dict(zip(p, tab[k]))), f2(**dict(zip(p, tab[k])))) != res[k]:
                break
        else:
            print(p)