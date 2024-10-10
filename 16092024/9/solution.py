with open("9.txt") as f:
    lines = f.readlines()

lines = [list(map(int, i.strip().split("	"))) for i in lines]

amount = 0
for line in lines:
    if len(set(line)) == 6:
        continue
    if line.count(max(line)) != 1:
        continue
    s= 0
    for i in line:
        if (line.count(i) != 1):
            s+=i
    if (s < max(line)):
        amount+=1
print(amount)
