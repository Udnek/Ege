with open("9.txt") as file:
    lines = file.readlines()

lines = [list(map(int, (i.strip().split("	")))) for i in lines]

# a, a, b, b, c, d, e
# a, b, c, d, e

n = 0
for numbers in lines:
    f = None
    s = None
    unic = []
    stop = False
    for i in numbers:
        if numbers.count(i) == 2:
            if f is None or f == i:
                f = i
            elif s is None or s == i:
                s = i
            else:
                stop = True
        elif numbers.count(i) == 1:
            unic.append(i)
        else:
            stop = True

    if len(unic) != 3:
        stop = True

    if stop:
        continue

    if (sum(unic)/3) > ((f+s)/2):
        n += 1

print(n)

