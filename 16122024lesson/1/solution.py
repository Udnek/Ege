from itertools import *
r = "14 15 16 " \
    "23 25 27 " \
    "32 37 38 " \
    "41 46 " \
    "51 52 56 58 " \
    "61 64 65 67 " \
    "72 73 76 78 " \
    "83 85 87"

s = "АБ АД " \
    "БА БД БЕ БВ " \
    "ВБ ВЕ ВЖ ВИ ВГ " \
    "ГВ ГИ " \
    "ИГ ИВ ИЖ " \
    "ЖИ ЖВ ЖЕ " \
    "ЕД ЕБ ЕВ ЕЖ " \
    "ДА ДБ ДЕ"

for p in permutations(set(s.replace(" ", ""))):
    c = s
    for k, v in enumerate(p): c = c.replace(v, str(k+1))
    #print(c)
    res = (set(c.split(" ")) - set(r.split(" ")))
    res1 = (set(r.split(" ")) - set(c.split(" ")))
    if res.__len__() <= 2 and res1.__len__() <= 2:
        print(res)
        print(res1)
        print(p)
        print()
    #print()
    # print(" ")
    # print(set(c.split(" ")) - set(r.split(" ")))
    # print(len(set(c.split(" "))-set(r.split(" "))))

