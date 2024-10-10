# def f(n):
#     if (n < 11):
#         return n
#     return n + f(n-1)
#
# print(f(2024) - f(2021))

def f(n):
    s = 0
    for i in range(11, n + 1):
        s += i
    return s
print(f(2024) - f(2021))
