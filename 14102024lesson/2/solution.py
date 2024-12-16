w = sorted("В, Е, Р, О, Н, И, К, А".split(", "))

def first():
    from itertools import product

    i = 0
    for p in product(w, repeat=3):
        if p.count("В") != 1: continue
        i += 1
        if p.count("А") == 0:
            print(p, i)
            return

def second():
    i = 0
    for a0 in w:
        for a1 in w:
            for a2 in w:
                p = f"{a0}{a1}{a2}"
                if p.count("В") != 1: continue
                i += 1
                if p.count("А") == 0:
                    print(p, i)
                    return

first()
second()