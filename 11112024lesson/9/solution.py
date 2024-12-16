from itertools import permutations

with open("task.txt") as file:
    lines = file.readlines()

lines = [[int(i) for i in row.strip().split("\t")] for row in lines]

print(len(lines))
amount = 0
for a, b, c in lines:
    p0 = a*b
    p1 = b*c
    p2 = c*a
    for pa,pb,pc in permutations([p0, p1, p2]):
        if (pa + pb < pc):
            amount += 1
            break
print(amount)