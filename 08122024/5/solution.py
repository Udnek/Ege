def f(n):
    k = str(n)
    s = [int(k[0])+int(k[1]), int(k[1])+int(k[2]), int(k[2])+int(k[3])]
    s.remove(min(s))
    s = sorted(s)
    return int(str(s[0])+str(s[1]))

for i in range(1000, 9999):
    if (f(i) == 1215):
        print(i)
        break