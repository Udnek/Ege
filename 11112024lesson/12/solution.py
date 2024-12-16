s = "8"*125

while True:
    if (s.__contains__("333")):
        s = s.replace("333", "8", 1)
    elif (s.__contains__("888")):
        s = s.replace("888", "3", 1)
    else:
        break
print(s)
