world = "тридц"

file = open("10.txt", encoding="utf8")

for i in file.readlines():
    worlds = i.split(" ")
    printNext = False
    for w in worlds:
        if printNext:
            printNext = False
            print(w)
        if w.startswith(world):
            print(w, end=" ")
            printNext = True