from itertools import *
r = "12 14 17 " \
    "21 24 28 " \
    "35 37 38 " \
    "41 42 46 " \
    "53 58 " \
    "64 67 " \
    "71 73 76 " \
    "82 83 85"
s = "AB AH AE " \
    "BA BH " \
    "HB HA HF " \
    "FH FG FD " \
    "DF DC " \
    "CD CG CE " \
    "GF GC GE " \
    "EA EG EC"
for p in permutations(set(s.replace(" ", ""))):
    c = s
    for k, v in enumerate(p): c = c.replace(v, str(k+1))
    if set(c.split(" ")) == set(r.split(" ")):
        print(p)