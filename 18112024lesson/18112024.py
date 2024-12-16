# 72559
from itertools import *

unknown_roads = "13 14 15 18 26 27 28 31 34 35 37 41 43 46 47 51 53 58 62 64 67 68 72 73 74 76 81 82 85 86"
roads = "AБ АВ АГ АЖ БА БВ БД БИ ИБ ИД ИЕ ИЖ ЖИ ЖЕ ЖГ ЖА ГА ГЖ ГЕ ЕГ ЕЖ ЕД ЕИ ДЕ ДВ ДБ ДИ ВА ВБ ВД"

ids = sorted(set(roads.replace(" ", "")))
for p in permutations(ids):
    cache = unknown_roads
    for k, v in enumerate(p):
        cache = cache.replace(str(k+1), v)
    if set(cache.split(" ")) == set(roads.split(" ")):
        print(dict(enumerate(p)))







# unic = set(g.replace(' ', ''))
# for p in permutations(unic):
#     nt = t
#     for i, v in enumerate(p):
#         nt = nt.replace(str(i + 1), v)
#     if set(g.split()) == set(nt.split()):
#         print(p)
