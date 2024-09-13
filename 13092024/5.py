def f(n):
    binary = bin(n)[2:]
    for i in range(2):
        s = sum(list(map(int, list(binary))))
        binary += str(s % 2)
    return int(binary, 2)

for i in range(0, 10312390):
    if (f(i)) > 97:
        print(f(i))
        break
