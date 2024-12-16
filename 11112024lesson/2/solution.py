from itertools import permutations, product

# ((x → y ) ≡ (z → w)) ∨ (x ∧ w).
def F(x, y, z, w):
    return ((x <= y) == (z <= w)) or (x and w)

for a, b, c, d, e, f in product([0, 1], repeat=6):
    tab = [(1, a, b, c),
           (1, 1, d, e),
           (1, 1, 1, f)]
    if (len(set(tab)) != 3): continue
    for p in permutations("xyzw"):
        if [F(**dict(zip(p, row))) for row in tab] == [0, 0, 0]:
            print(p)

