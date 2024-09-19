def move(stones, t):
    if t == 0:
        return stones+1
    elif t == 1:
        return stones+2
    else:
        return stones*3

for i in range(1, 64+1):

    sureWin = False
    for p0 in range(3):
        wins0 = 0
        for v0 in range(3):
            for p1 in range(3):
                finalWins = 0
                for v1 in range(3):

                    stones = move(i, p0)
                    if stones > 64:
                        break
                    stones = move(stones, v0)
                    if stones > 64:
                        finalWins += 1
                        continue
                    stones = move(stones, p1)
                    if stones > 64:
                        break
                    stones = move(stones, v1)

                    if stones > 64:
                        finalWins += 1

                if finalWins == 3:
                    preWins += 1

        if ()