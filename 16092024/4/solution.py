from itertools import permutations, product

exists = ["00", "1001", "1010","110","0101","011","111","0100", '1000']

for l in range(6):
    for p in product(["0","1"], repeat=l):
        p = "".join(p)
        gg = True
        for e in exists:
            if (e.startswith(p) or p.startswith(e)):
                gg = False
        if (gg):
            print(p)
