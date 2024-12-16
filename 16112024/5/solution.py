def f(n):
    b = bin(n)[2:]
    if n % 2 == 0:
        b += "11"
    else:
        b = "1"+b+"10"
    return int(b, 2)

mx = -float("inf")
#  123_456_789
for i in range(456_789_012, 455_789_000, -2):
    if f(i) > mx: mx = f(i)
print()
print(mx)