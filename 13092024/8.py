letters = "А, В, Т, О, Р".split(", ")
index = 0

for a in letters:
    for b in letters:
        for c in letters:
            for d in letters:
                index += 1
                if a+b+c+d == "ТАРА":
                    print(index)
                    break


