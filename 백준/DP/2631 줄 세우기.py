# 배열에서 LIS 외의 인원을 옮기면 최소로 옮기는 것.

n = int(input())
arr = [int(input()) for _ in range(n)]

dp = [1]*n

for i in range(1, n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

result = max(dp)
print(n-result)