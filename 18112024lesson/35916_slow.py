from itertools import permutations

with open("27-A.txt") as f:
    lines = [int(i) for i in f.readlines()]
lines.pop(0)
min_sum = float('inf')
for p in permutations(lines, r=3):
    if len(set(p)) != 3: continue
    if sum(p) % 3 == 0:
        if sum(p) < min_sum: min_sum = sum(p)

print(min_sum)
