
s = "8"*99 + "1"

def cont(i):
    return s.count(i) > 0

def rep(i, j):
    global s
    s = s.replace(i, j, 1)

while cont("133") or cont("881"):
    if cont("133"):
        rep("133", "81")
    else:
        rep("881", "13")

print(s)