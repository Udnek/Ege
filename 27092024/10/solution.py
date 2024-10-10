n = 0
letters = ["А", "К", "Р", "У"]
for i in letters:
    for j in letters:
        for k in letters:
            for l in letters:
                for m in letters:
                    n += 1
                    if (n == 450):
                        print(f"{i}{j}{k}{l}{m}")

