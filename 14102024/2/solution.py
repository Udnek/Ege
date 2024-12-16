from itertools import product, permutations


def f(x, y, z, w):
    return ((x and not y) <= (not z or not w)) and ((w <= x) or y)

for a, b, c, d, e, e1 in product([0, 1], repeat=6):
    tab = [(1, a, 1, 1),
           (0, b, c, 0),
           (1, d, e, e1)]
    if len(set(tab)) != 3: continue
    for p in permutations("xyzw"):
        test = []
        for row in tab:
            v = dict(zip(p, row))
            test.append(f(**v))
        if test == [0, 0, 0]:
            print(p)
