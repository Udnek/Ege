from itertools import product, permutations

def f(x,y,z,w):
    return ((y or z) <= (z and w)) == (not ((x and z) <= (w or y)))

for a1, a2 in product([0, 1], repeat=2):
    sheet = [(a1, 1, 1, 1), (0, 0, 0, a2), (1, 1, 0, 0)]
    for p in permutations("xyzw"):
        c = [f(**dict(zip(p, row))) for row in sheet]
        if (c == [1,1,1]):
            print(p)