a = "26x98"
b = "4x296"
nums = list(range(10))
nums += ["a", "b", "c"]

def calc(i):
    ad = int(a.replace("x", str(i)), 13)
    bd = int(b.replace("x", str(i)), 13)
    return ad + bd

for i in nums:
    if calc(i) % 34 == 0:
        print(calc(i), calc(i)/34)