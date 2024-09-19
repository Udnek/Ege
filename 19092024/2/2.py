
def F(x, y, z, w):
    return (not ((x or not y) and (not z == w))) or (y and z)

print("x y z w")
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if F(x, y, z, w):
                    continue
                print(x, y, z, w)