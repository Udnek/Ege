w = list(range(9))

def first():
    from itertools import product
    i = 0
    for p in product(w, repeat=5):
        if p[0] != 0 and tuple(sorted(p)[::-1]) == p and len(set(p)) == 5:
            i += 1
    print(i)

def second():
    i = 0
    for a0 in w:
        for a1 in w:
            for a2 in w:
                for a3 in w:
                    for a4 in w:
                        s = f"{a0}{a1}{a2}{a3}{a4}"
                        if s[0] != "0" and "".join(sorted(s)[::-1]) == s and len(set(s)) == 5:
                            i+=1
    print(i)


first()
second()
