from itertools import product, permutations

# (x ≡ y ) ∨ ((y ∨ z) → x).
def f(x,y,z):
    return (x==y) or ((y or z) <= x)

for a0, a1, a2 in product([0, 1], repeat=3):
    #tab = [[a0, a1],[1, a2],[1, 1]]
    tuple
    sheet = [(a0, 1, 1), (a1, a2, 1)]
    if len(set(sheet)) != 2: continue

    for x, y, z in permutations("xyz"):
        c = [f(**dict(zip([x,y,z], row))) for row in sheet] == [0, 0]
        if (c):
            print(x,y,z)



# with open("Я_памятник_себе_воздвиг_нерукотворный.txt") as f:
#     lines = f.readlines()
#
# amount = {}
#
# for line in lines:
#     for s in line:
#         if amount.keys().__contains__(s):
#             amount[s] += 1
#         else:
#             amount[s] = 1
#
# for k, v in amount.items():
#     print(k, v)