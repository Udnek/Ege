# +1
# +2
# *3

def go(stones, t, moves):
    if stones > 64:
        print(moves)
        return True

    newMoves = moves[:]
    newMoves.append(t)

    return go(stones*3, 3, newMoves) or go(stones+2, 2, newMoves) or go(stones+1, 1, newMoves)


def move(stones, t):
    if t == 0:
        return stones+1
    elif t == 1:
        return stones+2
    else:
        return stones*3

for i in range(1, 64+1):

    for p in range(3):
        for v in range(3):

            stones = move(i, p)
            stones = move(stones, v)

            if stones > 64:
                print(i, p, v)