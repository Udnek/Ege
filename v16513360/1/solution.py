# (x → (y ≡ w)) ∧ (y ≡ (w → z)).
print("x y z w f")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (x <= (y == w)) and (y == (w <= z))
                #if (y == 0 and w == 0 and (z == 1 or x == 1) and not f):
                if y and not x and not w and z:
                    print(x, y, z, w, f)


# - - - -