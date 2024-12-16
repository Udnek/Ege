from itertools import product

c = 0
for p in product("012345678", repeat=5):
    r = "".join(p)
    if r[0] == "0": continue
    if r.count("3") != 2: continue
    if r[0] == "2" and int(r[1]) % 2 == 1: continue
    if r[4] == "2" and int(r[3]) % 2 == 1: continue
    for j in range(1, 3+1):
        if r[j] != "2": continue
        if int(r[j-1]) % 2 == 1: break
        if int(r[j+1]) % 2 == 1: break
    else:
        c += 1
print(c)