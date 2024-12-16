w = list("РОСОМАХА")
vowels = list("РСМХ")
consonant = list("ОА")

def first():
    from itertools import permutations
    all = set()
    for p in permutations(w):
        for i in range(len(p)-1):
            a = p[i]
            b = p[i+1]
            if (vowels.__contains__(a) and vowels.__contains__(b)) or (consonant.__contains__(a) and consonant.__contains__(b)):
                break
        else:
            all.add(p)
    print(len(all))

def second():
    from itertools import product
    all = set()
    for p in product(w, repeat=8):
        for l in w:
            if p.count(l) != w.count(l): break
        else:
            for i in range(len(p) - 1):
                a = p[i]
                b = p[i + 1]
                if (vowels.__contains__(a) and vowels.__contains__(b)) or (
                        consonant.__contains__(a) and consonant.__contains__(b)):
                    break
            else:
                all.add(p)


    print(len(all))


first()
second()
