def who(move):
    return (move + 1) % 2
def who_wins(a, move=0):
    if a <= 19: return who(move)
    if move == 2: return 0
    wins = [who_wins(a-1, move+1)]
    if a%3 == 0: wins.append(who_wins(a//3, move+1))
    else: wins.append(who_wins(a-2, move+1))
    if a%5 == 0: wins.append(who_wins(a//5, move+1))
    else: wins.append(who_wins(a-3, move+1))
    #return wins
    if who(move) == 0:
        return any(wins)
    return all(wins)

for i in range(20, 30):
    if who_wins(i): print(i)

