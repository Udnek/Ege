with open("task.txt") as f:
    lines = f.readlines()

lines = [list(map(int, line.strip().split("	"))) for line in lines]
total = 0
for line in lines:
    s = [i for i in line if line.count(i) == 3]
    d = [i for i in line if line.count(i) == 1]
    if not (len(s) == 3 and len(d) == 3): continue
    if sum(s) ** 2 > sum(d) ** 2:
        total += 1
print(total)

    # mp = {}
    # for i in line:
    #     mp[i] = mp.get(i, 0) + 1
    # s = 0
    # d = 0
    # if list(mp.values()).count(3) == 1 and list(mp.values()).count(1) == 3:
    #     for k, v in mp.items():
    #         if v == 3: s += k
    #         else: d += k
    #     if s**2 > d**2: total += 1