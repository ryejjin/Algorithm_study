##중복조합
from itertools import combinations_with_replacement
n, m = map(int, input().split())

nums = []
for i in range(1, n+1):
    nums.append(i)

anw = combinations_with_replacement(nums, m)
ls = []
for k in anw:
    ls.append(list(map(int, k)))

for j in ls:
    print(*j)