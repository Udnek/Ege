w = list("ГЕРАСИМ")
vowels = list("ГРСМ")
consonant = list("ЕАИ")

def first():
    from itertools import permutations
    c = 0
    for p in permutations(w):
        for i in range(len(p)-1):
            a = p[i]
            b = p[i+1]
            #if (vowels.__contains__(a) and vowels.__contains__(b)) or (consonant.__contains__(a) and consonant.__contains__(b)):
            if (a in vowels and b in vowels) or (a in consonant and b in consonant):
                break
        else:
            c += 1
    print(c)

def second():
    print(4*3*3*2*2*1)


first()
second()
