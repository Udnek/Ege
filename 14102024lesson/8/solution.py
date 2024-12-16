def first():
    from itertools import product
    w = "A, B, C, D".split(", ")
    i = 0
    for f in ["X", "Y", "Z"]:
        for p in product(w, repeat=3):
            i += 1
    print(i)


def second():
    print(3* (4**3))


first()
second()
