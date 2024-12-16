with open("18_1.txt") as f:
    lines = f.readlines()

lines = [float(i.strip()) for i in lines]
print(lines)
max_sum = -float("inf")
for i in range(len(lines)-1):
    s = lines[i]
    for j in range(i, len(lines)-1):
        a, b = lines[j], lines[j+1]
        if abs(b - a) > 10: break
        s += b
    if s > max_sum:
        max_sum = s

print(max_sum)
