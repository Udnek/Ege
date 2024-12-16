w = tuple("МИТРОФАН")
vowels = tuple("ИОА")
consonants = tuple("МТРФН")

def first():
    c = 0
    from itertools import permutations
    for p in permutations(w, r=6):
        vs = 0
        for i in vowels: vs += p.count(i)
        cs = 0
        for i in consonants: cs += p.count(i)

        if cs <= vs: continue
        for i in range(len(p)-1):
            a = p[i]
            b = p[i+1]
            if vowels.__contains__(a) and vowels.__contains__(b):
                break
        else:
            c += 1
    print(c)

def second():
    from itertools import product
    all = set()
    for p in product(w, repeat=6):
        if (len(set(p)) != 6):
            continue

        s = 0
        for i in vowels: s += p.count(i)
        for i in consonants: s -= p.count(i)
        if s>=0: continue

        for i in range(len(p) - 1):
            a = p[i]
            b = p[i+1]
            if vowels.__contains__(a) and vowels.__contains__(b):
                break
        else:
            all.add(p)

    print(len(all))
first()
second()
