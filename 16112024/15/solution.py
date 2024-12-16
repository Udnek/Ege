
def f(n):
    if n < 15: return n
    return f(n % 15) * f(n // 15)

total = 0
for i in range(1, 3**40):
    if f(i) == 7560: total += 1