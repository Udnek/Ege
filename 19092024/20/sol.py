def move(stones, t):
    if t == 0:
        return stones+1
    elif t == 1:
        return stones+2
    else:
        return stones*3

for i in range(1, 64+1):

    for p0 in range(3):
        hasWins = False
        for v in range(3):
            wins = 0
            for p1 in range(3):

                stones = move(i, p0)
                if stones > 64:
                    break
                stones = move(stones, v)
                if stones > 64:
                    break
                stones = move(stones, p1)

                if stones > 64:
                    wins += 1

            if wins == 3:
                hasWins = True

        if hasWins:
            print(i)
            break