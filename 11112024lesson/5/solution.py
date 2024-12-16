def f(n):
    b = bin(n)[2:]
    if (n % 5 == 0): b += bin(5)[2:]
    else: b += "1"
    if (int(b, 2) % 7 == 0): b += bin(7)[2:]
    else: b += "1"
    return int(b, 2)

for i in range(1, 1_000_000):
    if (f(i) <  1_728_404):
        print(i, f(i))
