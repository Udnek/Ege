with open("17.txt") as f:
    lines = f.readlines()

lines = list(map(int, lines))
mn = min(lines) % 3
mx = max(lines) % 7

amount = 0
s = 0
for i in range(len(lines)-1):
    a = lines[i]
    b = lines[i+1]
    if (a % 3 == mn or b % 3 == mn) and (a % 7 == mx or b % 7 == mx):
        amount += 1
        s = max(s, a + b)
print(amount, s)

