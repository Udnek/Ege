# def f(n):
#     r = ""
#     while n > 0:
#         r = str(n % 4) + r
#         n //= 4
#     return r

# print(f(122))
from itertools import product

count = 0
for a,b,c in product("0123", repeat=3):
    if (a == "0"): continue
    if (int(a) + int(c) > int(b)): count += 1
print(count)