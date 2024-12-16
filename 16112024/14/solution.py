# ((x&45 > 0) ∨ (x&89 > 0)) → (x&A > 0)

for A in range(0, 99999):
    for x in range(0, 99999):
        if ((x&45 > 0) or (x&89 > 0)) <= (x&A > 0): continue
        break
    else:
        print(A)
        break