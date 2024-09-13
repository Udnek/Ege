file = open("9.txt")

def f(a, b, c, d):
    return tr(a, b, c) or tr(a, b, d) or tr(a, c, d) or tr(b, c, d)
def tr(a, b, c):
    return (a + b > c) and (a + c > b) and (b + c > a)

amount = 0
for line in file.readlines():
    nums = list(map(int, line.replace("\n", "").split("\t")))
    if not f(nums[0], nums[1], nums[2], nums[3]):
        amount += 1

print(amount)