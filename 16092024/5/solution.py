def f(n):
    b = str(bin(n))[2:]
    summ = sum(list(map(int, b)))
    b = b + str(summ % 2)
    summ = sum(list(map(int, b)))
    b = b + str(summ % 2)
    return int(b, 2)

mx = 0
for i in range(1, 999999999):
    a = f(i)
    if (a > mx and a < 100):
        mx = a
        print(a)