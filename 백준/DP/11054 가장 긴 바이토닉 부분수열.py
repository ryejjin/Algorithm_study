n = int(input())
arr = list(map(int, input().split()))

dp1 = [1] * n
dp2 = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp1[i] = max(dp1[i], dp1[j]+1)

for i in range(n-1, -1, -1):
    for k in range(n-1, i-1, -1):
        if arr[k] < arr[i]:
            dp2[i] = max(dp2[i], dp2[k]+1)

dp = [0] * n
dp[0] = dp1[0]+dp2[0]-1
for i in range(1, n):
    dp[i] = max(dp[i-1], dp1[i]+dp2[i]-1)

# print(dp1)
# print(dp2)
# print(dp)
print(dp[-1])