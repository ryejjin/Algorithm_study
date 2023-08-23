# 값이 최소가 되게 하려면 '-' 이후의 값이 최대가 되면 된다
# 따라서 '-'를 기준으로 split 한 후 계산해주면 된다.

import sys
input = sys.stdin.readline

cals = list(input().split('-'))

nums = []
for cal in cals:
    temp = list(map(int, cal.split('+')))
    nums.append(sum(temp))

if len(nums) == 1:
    print(*nums)
else:
    res = nums[0]
    for i in range(1, len(nums)):
        res -= nums[i]
    print(res)