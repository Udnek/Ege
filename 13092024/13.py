def tobin(i):
    return bin(int(i))[2:]

ip = tobin(224)
address = tobin(192)

res = ""
for i in range(len(ip)):
    ipb = ip[i]
    adb = address[i]
    res += adb

    print(f"{ipb} && {str(adb)} = {adb}")

print(res)
print(int(res, 2))