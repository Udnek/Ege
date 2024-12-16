w = sorted(["К", "О", "М", "П", "Ь", "Т", "Е", "Р"])

def first():
    from itertools import product
    i = 0
    n = 0
    res = ""
    for p in product(w, repeat=5):
        i += 1
        if p.count("К") == 0 and p.count("Р") == 2:
            res = p
            n = i
    print(res, n)

def second():
    i = 0
    n = 0
    res = ""
    for a0 in w:
        for a1 in w:
            for a2 in w:
                for a3 in w:
                    for a4 in w:
                        i += 1
                        p = f"{a0}{a1}{a2}{a3}{a4}"
                        if p.count("К") == 0 and p.count("Р") == 2:
                            res = p
                            n = i
    print(res, n)



first()
second()