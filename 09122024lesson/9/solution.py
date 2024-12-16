from itertools import *
# def fact(n):
#     x = 1
#     for i in range(1, n+1): x *= i
#     return x
# c = 0
# c = 2*(fact(4*4)/fact(5) + fact(4*4)/fact(6))
# print(c)



# for e in combinations("2468"*4, r=6):
#     for o in combinations("1357"*4, r=5):
#         c += 1
# c = len(list(combinations("2468"*4, r=6))) * len(list(combinations("2468"*4, r=5)))
# print(c*2)
e = "2468"
o = "1357"
c = 0
for p in product(*[e, o]*5+[e]):
    for i in p:
        if p.count(i) > 4: break
    else:
        c+=1
print(c*2)