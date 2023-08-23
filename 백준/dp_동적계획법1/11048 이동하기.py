n, m = map(int, input().split())
arr = [[0]+list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(m+1) for _ in range(n)]
dp[0][0] = arr[0][0]

for i in range(1, m+1):
    dp[0][i] = dp[0][i-1] + arr[0][i]

for j in range(1, n):
    dp[j][1] = dp[j-1][1] + arr[j][1]

for k in range(1, n):
    for l in range(1, m+1):
        dp[k][l] = max(dp[k-1][l], dp[k][l-1], dp[k-1][l-1]) + arr[k][l]

print(dp[-1][-1])