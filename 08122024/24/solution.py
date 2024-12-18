with open("24.txt") as f:
    d = f.readline().replace("A", " A ").replace("B", " B ").split(" ")

mx = 0
for i in range(0, d.__len__()-4):
    s = ""
    for j in range(i,min(i+5, d.__len__())):
        s += d[j]
        if s.count("A") == 1 and s.count("B") == 1:
            if len(s) > mx: mx = len(s)
print(mx)