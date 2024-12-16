
def whoWin(a, b, move=-1):
    if a+b>=58: return move%2
    if move == 2: return 0
    wins = [whoWin(a*2,b,move+1),
            whoWin(a,b*2,move+1),
            whoWin(a+1,b,move+1),
            whoWin(a,b+1,move+1)]
    return all(wins)
for S in range(1, 53+1):
    print(S, whoWin(5, S))