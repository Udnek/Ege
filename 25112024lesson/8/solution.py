from itertools import product, permutations

t = 0
for p in product("01a", repeat=8):
    if p[0] != "0" and p.count("a") <= 4 and p.count("0") == 2:
        t += 5**p.count("a") * 9**p.count("1")
print(t)