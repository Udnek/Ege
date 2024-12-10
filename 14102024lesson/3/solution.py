from itertools import product

w = sorted(["К", "О", "М", "П", "Ь", "Т", "Е", "Р"])
i = 0
res = ""
for p in product(w, repeat=len(w)):
    i += 1
    if p.count("К") == 0 and p.count("Р") == 2:
        res = p
print(res)
