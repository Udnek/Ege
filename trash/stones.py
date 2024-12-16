def move(x, mt, count=0):
    if x > 56: return count%2 == 0
    print(x, end=" ")
    if mt == 0: x += 1
    if mt == 1: x += 2
    if mt == 2: x *= 2
    count += 1
    print(x)
    reses = [move(x, 0, count), move(x, 1, count), move(x, 2, count)]
    if count % 2 == 1: return any(reses)
    else: all(reses)


print(19,[s for s in range(1,77+1) if move(4,s,2)])
print(20,[s for s in range(1,77+1) if not move(4,s,1) and move(4,s,3)])
print(21,[s for s in range(1,77+1) if not move(4,s,2) and move(4,s,4)])