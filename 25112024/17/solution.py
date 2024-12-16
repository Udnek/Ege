import sys
sys.setrecursionlimit(2024)

def f(n):
    if n < 7: return 7
    return 2*n + f(n-1)

print(f(2024)-f(2023))