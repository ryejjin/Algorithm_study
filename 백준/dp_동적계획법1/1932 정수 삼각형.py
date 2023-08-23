n = int(input())
arr = [[0]]+[[0]+list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(n+1) for _ in range(n+1)]
if n == 1:
    print(arr[1][1])
else:
    dp[1][1] = arr[1][1]
    dp[2][1] = dp[1][1]+arr[2][1]
    dp[2][2] = dp[1][1]+arr[2][2]
    for i in range(3, n+1):
        for j in range(1, i+1):
            dp[i][j] = max(dp[i-1][j-1],dp[i-1][j])+arr[i][j]
    print(max(dp[n]))