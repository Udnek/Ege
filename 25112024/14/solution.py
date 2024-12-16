import ipaddress
from itertools import permutations
a = "7.2"
b = "53"
v = "102."
g = "84.1"
for p in permutations([a,b,v,g]):
    try:
        ipaddress.ip_network("".join(p), True)
        print(p)
    except:
        pass
print(c)