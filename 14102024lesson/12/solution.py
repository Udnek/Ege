w = list(range(8))

def first():
    from itertools import product
    c = 0
    for p in product(w, repeat=5):
        if p[0] == 0: continue
        if p.count(6) != 1: continue
        i = p.index(6)
        toCheck = []
        if i > 0: toCheck.append(p[i-1])
        if i < len(p)-1: toCheck.append(p[i + 1])
        for x in toCheck:
            if x % 2 != 0: break
        else:
            c += 1
    print(c)

def second():
    c = 0
    for a0 in range(1, 8):
        for a1 in range(8):
            for a2 in range(8):
                for a3 in range(8):
                    for a4 in range(8):
                        p = f"{a0}{a1}{a2}{a3}{a4}"
                        if p.count("6") != 1: continue
                        i = p.index("6")
                        toCheck = []
                        if i > 0: toCheck.append(p[i - 1])
                        if i < len(p) - 1: toCheck.append(p[i + 1])
                        for x in toCheck:
                            if int(x) % 2 != 0: break
                        else:
                            c += 1
    print(c)

first()
second()
