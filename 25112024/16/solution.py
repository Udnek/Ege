
def f(a, x):
    return ((x&35 != 0) or (x&22 != 0)) <= ((x&15 == 0) <= (x&a != 0))
for a in range(0, 10000):
    for x in range(0, 1000000):
        if not f(a, x): break
    else:
        print(a)
        break