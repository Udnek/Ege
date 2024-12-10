from itertools import permutations, product

i = 0
for a,b,c,d in product(["К","Л","Р","Т"], repeat=4):
    i+=1
    s = f"{a}{b}{c}{d}"
    if (i == 67):
        print(s)