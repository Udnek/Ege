import math

from itertools import combinations

def isPrime(n):
    for i in range(2, int(math.sqrt(n).__round__())):
        if n % i == 0: return False
    return True

primes = []
i = 2
while primes.__len__() < 10_000:
    if isPrime(i): primes.append(i)
    i+=1

def find(n):
    divs = []
    for i in range(2, int(math.sqrt(n).__round__())):
        if n % i == 0:
            if divs.__len__() >= 2:
                for c in combinations(divs, r=divs.__len__()):
                    r = 1
                    for j in c: r *= j
                    if n % r == 0:
                        if r < i:
                            divs.append(i)
            if divs.__len__() == 5:
                divs = sorted(divs)
                return divs[0]*divs[1]*divs[2]*divs[3]*divs[4]
            else:
                divs.append(i)

    return 0
i = 500_000_001
while True:
    res = find(i)
    if 0 < res < i:
        print(res)
    i+=1