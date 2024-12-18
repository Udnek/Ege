with open("task.txt") as f:
    lines = f.readlines()

lines = [list(map(int, i.replace("\n", "").split("\t"))) for i in lines]

def get(y, x):
    res = []
    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            if i == y and j == x: continue
            if i < 0 or j < 0: continue
            if i >= (lines.__len__()-1) or j >= (lines[0].__len__()-1): continue
            res.append(lines[i][j])
    return res

def test(y, x):
    if lines[y].count(lines[y][x]) > 1: return False
    for n in get(y, x):
        if n > lines[y][x]: return True
    return False

c = 0
for i in range(len(lines)):
    if len(set(lines[i])) == len(lines[i]): continue
    cool = 0
    for j in range(len(lines[i])):
        cool += int(test(i, j))
    if cool < 3: continue
    c += 1

print(c)