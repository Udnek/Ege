

with open("task.txt") as file:
    lines = file.readlines()

lines = [list(map(int, i.strip().split("	"))) for i in lines]

count = 0
for i in lines:
    i.sort()
    if i[0]**2 + i[1]**2 > i[2]**2:
        count+=1

print(count)