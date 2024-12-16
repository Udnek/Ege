from itertools import *

r = "15 17 18 24 27 28 34 35 37 42 43 47 51 53 56 65 68 71 72 73 74 81 82 86"
s = "АБ АГ АЕ БА БВ БГ ВБ ВИ ВД ДВ ДЖ ИВ ИЖ ЖИ ЖД ЖЕ ЕЖ ЕГ ЕА ГА ГБ ГЕ"

for p in permutations(set(s.replace(" ", ""))):
    c = s
    for k, v in enumerate(p): c = c.replace(v, str(k+1))
    d = set(r.split(" ")) - set(c.split(" "))
    if d.__len__() <= 2:
        print(d)
