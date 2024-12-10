w = "КЛРТ"
n = 0
for i in w:
    for j in w:
        for k in w:
            for l in w:
                n+=1
                s = f"{i}{j}{k}{l}"
                if (n == 67): print(s)