import math
def f(n):
    b = bin(n)[2:]
    b += bin(n%3)[2:].zfill(2)
    b += bin(int(b, 2) % 5)[2:].zfill(3)
    return int(b, 2)

def d(n):
    k = n*2*2+n%3
    return k*2*2*2+k%5

c = 0
for i in range(math.ceil(1_222_222_222/(2**6)), math.ceil(1_555_555_666/(2**4)), 1):
    if 1_222_222_222 <= d(i) <= 1_555_555_666: c+=1
print(c)