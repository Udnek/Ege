def F(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n % 2 == 0:
        return (3*n + F(n-3))//3
    else:
        return (7*n + F(n-1) - F(n-2)) // 5

print(F(35))