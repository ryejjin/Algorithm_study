# top-down
# dp에는 i번째 일까지 했을때 얻을 수 있는 최대 수익
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n+1)]
#
for i in range(n-1, -1, -1):
    if i + arr[i][0] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], arr[i][1] + dp[i+arr[i][0]])

print(dp[0])
#-------------------------------------------------

# bottom-up
# for i in range(n):
#     for j in range(i+arr[i][0], n+1):
#         if dp[j] < dp[i] + arr[i][1]:
#             dp[j] = dp[i] + arr[i][1]
# print(dp[-1])