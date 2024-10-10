with open("task.txt") as file:
    lines = file.readlines()

lines = [list(map(int, i.strip().split("	"))) for i in lines]

count = 0
for i in lines:
    if len(set(i)) == 6:
        mm = max(i) + min(i)
        o = sum(i)-mm
        if mm/2 > o/4:
            count += 1

print(count)