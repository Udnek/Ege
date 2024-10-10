# from fnmatch import *
# from itertools import product, combinations, permutations
#
# for i in permutations("123", 1):
#     print(i)
# s = "112A"
# for i in product(s, "mnk"):
#     print(i)

# a = {1,2,3}
# b = {1,2,5}
# print(a&b)

#print(fnmatch("123", "[12][2][3]"))

# def test(n):
#     if (n%2 != 0):
#         return False
#
#     n = list(map(int, list(str(n))))
#
#     if (n[0] == n[-1]):
#         return False
#     if (n[0] not in [5, 6, 8]):
#         return False
#     if (n[0] == n[2]):
#         return False
#     if (n[2] not in [5, 7, 9]):
#         return False
#
#     return True
#
# print(test(56789))
# print(test(85758))
# print(test(77700))
# print(test(50786))