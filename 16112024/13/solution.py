
a = "y04x5"
b = "253xy"

mn = 999999999999
for x in "01234567":
    for y in "1234567":
        na = int(a.replace("x", x).replace("y", y), 11)
        nb = int(b.replace("x", x).replace("y", y), 8)
        if (na + nb) % 117 == 0 and (na + nb) < mn:
            mn = na + nb
print(mn, mn / 117)

