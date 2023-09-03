import sys
input = sys.stdin.readline

n = int(input())
arr = [[-1]*3] + [list(map(int, input().split())) for _ in range(n)]
INF = int(1e9)

R, G, B = 0, 1, 2
ans = INF

for i in [R, G, B]:
    dp = [[-1]*3 for _ in range(n+1)]

    dp[1] = [INF, INF, INF]
    dp[1][i] = arr[1][i]

    for j in range(2, n+1):
        dp[j][R] = min(dp[j-1][G], dp[j-1][B]) + arr[j][R]
        dp[j][G] = min(dp[j-1][R], dp[j-1][B]) + arr[j][G]
        dp[j][B] = min(dp[j-1][R], dp[j-1][G]) + arr[j][B]
    dp[n][i] = INF
    ans = min(ans, min(dp[n]))

print(ans)