from itertools import *

r = "13 14 16 25 27 31 34 35 41 43 45 46 47 52 53 54 61 64 67 72 74 76"
s = "AB AG BA BC BD CB CD CE CF CG DB DC DE EC ED EF FC FE FG GA GC GF"

uniq = set(s.replace(" ", ""))
for p in permutations(uniq):
    c = s
    for k, v in enumerate(p): c = c.replace(v, str(k+1))
    if set(r.split(" ")) == set(c.split(" ")):
        print(p)