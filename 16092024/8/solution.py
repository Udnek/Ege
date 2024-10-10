from itertools import permutations

word = "ПАРАБОЛА"
vowels = "АО"
consonants = "ПРБЛ"

amout = 0
for p in permutations(word):
    gg = False
    for l in range(len(p)-1):
        a = p[l]
        b = p[l+1]
        if (a in vowels and b in vowels) or (a in consonants and b in consonants):
            gg = True
    if (not gg):
        amout += 1

print(amout)