import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [[0]*n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for i in range(n-1):
    if arr[i] == arr[i+1]:
        dp[i][i+1] = 1
    else:
        dp[i][i+1] = 0

for i in range(3, n+1):
    for start in range(n-i+1):
        end = start+i-1
        if arr[start] == arr[end] and dp[start+1][end-1] == 1:
            dp[start][end] = 1

m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])