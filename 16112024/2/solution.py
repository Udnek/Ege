from itertools import product, permutations

def f(x, y, z, w):
    return (x <= (z <= w)) and (z <= (y != w))

for a in product([0, 1], repeat=6):
    tab = [(a[0], 0, 0, 0),
           (a[1], a[2], 0, 0),
           (a[3], a[4], 0, a[5])]
    if len(set(tab)) != 3: continue
    for p in permutations("xyzw"):
        #print([f(**dict(zip(p, row))) for row in tab])
        if [f(**dict(zip(p, row))) for row in tab] == [0, 0, 0]:
            print(p)