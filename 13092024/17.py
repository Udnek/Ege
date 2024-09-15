file = open("17.txt")
nums = []
for line in file:
    nums.append(int(line))

mn = -float("inf")
for i in nums:
    if str(i)[-1] == '5' and i < mn:
        mn = i

amount = 0
mxsquare = 0
for i in range(len(nums)-1):
    a = nums[i]
    b = nums[i+1]
    if str(min(a, b))[-1] != '5':
        continue
    if not (a*a + b*b < mn*mn):
        continue
    if a*a + b*b > mxsquare:
        mxsquare = a*a + b*b

    amount += 1

print(amount, mxsquare)