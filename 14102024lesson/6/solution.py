w = sorted("М, А, Н, Г, У, С, Т".split(", "))

def first():
    from itertools import product
    n = 0
    res = "???"
    i = 0
    for p in product(w, repeat=6):
        i += 1
        if p[0] != "У" and p.count("М") == 2 and p.count("Г") <= 1:
            res = p
            n = i
    print(res, n)

def second():
    i = 0
    for a0 in w:
        for a1 in w:
            for a2 in w:
                for a3 in w:
                    for a4 in w:
                        for a5 in w:
                            p = f"{a0}{a1}{a2}{a3}{a4}{a5}"
                            i += 1
                            if not p.startswith("У") and p.count("М") == 2 and p.count("Г") <= 1:
                                res = p
                                n = i
    print(res, n)

first()
second()