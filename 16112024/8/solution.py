from itertools import product

total = 0
for p in product("01a", repeat=8):
    if p[0] == "0": continue
    if p.count("0") != 2: continue
    if p.count("a") > 4: continue
    total += 9 ** p.count("1") + 6**p.count("a")

print(total)
