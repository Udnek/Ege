from itertools import *

def test(n):
    s = str(n)
    if s.__contains__("1"): return False
    if set(s).__len__() != 5: return False
    for i in range(4):
        if int(s[i]) % 2 == int(s[i+1]) % 2:
            return False
    return True

c = 0
for p in product("01234567", repeat=5):
    if p[0] == "0": continue
    if test("".join(p)): c+=1
print(c)