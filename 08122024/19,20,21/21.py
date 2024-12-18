def who(move):
    return (move + 1) % 2

def has_strategy(a, must_win_on, move=0):
    if a <= 19:
        return who(move) == 1
    if must_win_on == move: return 0
    move += 1
    wins = [has_strategy(a - 1, must_win_on, move)]
    if a%3 == 0: wins.append(has_strategy(a // 3, must_win_on, move))
    else: wins.append(has_strategy(a - 2, must_win_on, move))
    if a%5 == 0: wins.append(has_strategy(a // 5, must_win_on, move))
    else: wins.append(has_strategy(a - 3, must_win_on, move))
    if who(move) == 1:
        return any(wins)
    return all(wins)

for i in range(20, 100):
    if (has_strategy(i, 2) or has_strategy(i, 4)) and not has_strategy(i, 2):
        print(i)