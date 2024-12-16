def f(n):
    while n.__contains__("111"):
        n = n\
            .replace("111", "2", 1)\
            .replace("222", "11", 1)\
            .replace("1", "2", 1)
    return n

# for i in range(10, 1000):
#     n = f(i*'1')
#     # 16(25), 16(10), 16(16)
#     if len(n) == n.count("2"):
#         if n == "2222":
#             print(i, n)
c = 0
for i in range(123_456_794, 678_901_234+1):
    n = i % 16
    if n == 9 or n == 10 or n == 0:
        c += 1
print(c)



# data = {}
# for i in range(5, 1000):
#     type = i % 10
#     n = f("1" * i)
#     nice = len(n) == n.count("2")
#
#     if nice:
#         data[type] = data.get(type, 0) + 1
#
#
# for k, v in data.items():
#     print(k, v)
