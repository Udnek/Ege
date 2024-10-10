from itertools import product

ip = list(map(int, "98.162.201.94".split(".")))
address = list(map(int, "98.162.192.0".split(".")))

def conj(a, b):
    return [a[0] & b[0], a[1] & b[1], a[2] & b[2], a[3] & b[3]]

amount = 0
for p in product(range(0, 256), repeat=4):
    if (conj(ip, p) == address):
        amount +=1