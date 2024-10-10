for x in range(0, 7):
    for y in range(0, 7):
        s = int(f"{y}{x}320", 7) + int(f"1{x}3{y}3", 9)
        if (s % 181 == 0):
            print(s // 181)