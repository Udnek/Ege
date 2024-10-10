

def f(s):

    def cont(a):
        return s.count(a) > 0

    while cont("52") or cont("2222") or cont("1122"):
        if cont("52"):
            s = s.replace("52", "11", 1)
        if cont("2222"):
            s = s.replace("2222", "5", 1)
        if cont("1122"):
            s = s.replace("1122", "25", 1)

    return s

for n in range(3, 10_001):
    news = f("5" + "2"*n)
    if sum(list(map(int, list(news)))) == 64:
        print(n)











