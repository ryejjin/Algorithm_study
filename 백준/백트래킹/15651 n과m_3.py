##중복순열
from itertools import product
n, m = map(int, input().split())

nums = []
for i in range(1, n+1):
    nums.append(i)

anw = product(nums, repeat = m)
ls = []
for k in anw:
    ls.append(list(map(int, k)))

for j in ls:
    print(*j)