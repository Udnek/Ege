def first():
    from itertools import permutations
    w = list("МАТВЕЙ")
    i = 0
    for p in permutations(w):
        if p[0] == "Й": continue
        if "".join(p).__contains__("АЕ"): continue
        i +=1
    print(i)

def second():
    from itertools import product
    w = list("МАТВЕЙ")
    i = 0
    for p in product(w, repeat=6):
        if p[0] == "Й": continue
        if "".join(p).__contains__("АЕ"): continue
        if len(set(p)) != 6: continue
        i += 1
    print(i)


first()
second()
