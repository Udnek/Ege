w = sorted("А, Б, З, И".split(", "))

def first():
    from itertools import product

    i = 0
    for p in product(w, repeat=4):
        i += 1
        #print(''.join(p))
        if ''.join(p) == "ИЗБА":
            print(p, i)
            return


def second():
    i = 0
    for a0 in w:
        for a1 in w:
            for a2 in w:
                for a3 in w:
                    i += 1
                    if f"{a0}{a1}{a2}{a3}" == "ИЗБА":
                        print(f"{a0}{a1}{a2}{a3}", i)
                        return

first()
second()