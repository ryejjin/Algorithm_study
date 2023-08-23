from collections import deque

n, k = map(int, input().split())
nums = []

for i in range(1, n+1):
    nums.append(i)

nums = deque(nums)

anw = []

while len(nums) > 0 :
    chk = 1
    while chk < k :
        a = nums.popleft()
        nums.append(a)
        chk += 1
    b = nums.popleft()
    anw.append(b)

print(f'<{", ".join(map(str, anw))}>')