
def f(n):
    a, b, c, d = int(str(n)[0]), int(str(n)[1]), int(str(n)[2]), int(str(n)[3])
    s = [a + b, b + c, c + d]
    s.remove(min(s))
    n = str(min(s)) + str(max(s))
    return n

for i in range(9999, 1000, -1):
    if f(i) == "1315":
        print(i)
        break