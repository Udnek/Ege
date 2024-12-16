w = sorted("А, Л, Г, О, Р, И, Т, М".split(", "))

def first():
    from itertools import product

    i = 0
    for p in product(w, repeat=4):
        i += 1
        if p[0] == "И" and p[1] == "Г":
            print(p, i)
            return

def second():
    i = 0
    for a0 in w:
        for a1 in w:
            for a2 in w:
                for a3 in w:
                    p = f"{a0}{a1}{a2}"
                    i += 1
                    if p.startswith("ИГ"):
                        print(p, i)
                        return

first()
second()