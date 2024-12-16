

def f(n):
    return int(bin(n)[2:] + bin(n%4)[2:], 2)


s = [f(i) for i in range(1, 1000000000)]
s = sorted(s)
mx = 0
for i in ra

