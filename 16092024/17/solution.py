with open("17.txt") as f:
    lines = f.readlines()

lines = list(map(int, lines))

mx = 0
amount = 0
for i in range(len(lines)-1):
    for j in range(i+1, len(lines)):
        a = lines[i]
        b = lines[j]
        s = a+b
        if s % 120 == 0:
            amount += 1
            if mx < s:
                mx = s

print(amount, mx)