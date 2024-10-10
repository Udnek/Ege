with open("task.txt") as file:
    lines = file.readlines()

lines = [list(map(int, i.strip().split("	"))) for i in lines]

count = 0
for line in lines:
    c = [line.count(j) for j in line]
    if not (c.count(1) == 3 and c.count(3) == 3):
        continue
    triple = line[c.index(3)]
    others = sum(line) - triple*3
    if (triple >= others/3):
        count+=1
print(count)