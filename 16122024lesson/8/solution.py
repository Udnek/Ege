from itertools import  *

def check(a, b):
    return (b > a and (a+b)%2 == 0) or (b < a and (a+b)%2 != 0)

def check_n(n):
    k = str(n)
    for i in range(len(k)-1):
        if not check(int(k[i]), int(k[i+1])): return False
    return True


goodies = dict()
for i in product(range(9), repeat=2):
    if check(i[0], i[1]):
        goodies[i[0]] = goodies.get(i[0], [])
        goodies[i[0]].append(i[1])

# for k, v in goodies.items():
#     print(k, v)

def tree(current, depth=0):
    if depth == 11: return 1
    c = 0
    for i in goodies[current]:
        c += tree(i, depth=depth+1)
    return c

c = 0
for i in range(1,9):
    c += tree(i)
print(c)
# "o, o+"
# "e, e+"
# "o+, e"
# "e+, o"

# c = 0
# for p in product("oe", repeat=12):
#     for i in range(12):
#         t = 1
#         if i == 0: t*=8




# for p in

# for i in range(10**12, 10**12+1000000000):
#     if check_n(i):
#         print(i, check_n(i))

# lets = "012345678"
# for p in product(lets, repeat=12):
#     if p[0] == "0"

