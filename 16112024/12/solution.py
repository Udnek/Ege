ip = 137
add = 136
for i in range(0, 256):
    if ip & i == add:
        print()
        print(bin(ip).zfill(8))
        print(bin(i).zfill(8), i)
        print(bin(add).zfill(8))
