import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dp_up = [[0]*(m+1) for _ in range(n+1)]
dp_down = [[0]*(m+1) for _ in range(n+1)]

for i in range(n, 0, -1):
    dp_up[i-1][0] = dp_up[i][0]+arr[i-1][0]
    dp_down[i-1][m-1] = dp_down[i][m-1]+arr[i-1][m-1]

for i in range(1, m):
    dp_up[n-1][i] = dp_up[n-1][i-1]+arr[n-1][i]
    dp_down[n-1][m-i-1] = dp_down[n-1][m-i]+arr[n-1][m-i-1]

for j in range(1, m):
    for i in range(n-2, -1, -1):
        dp_up[i][j] = max(dp_up[i][j-1], dp_up[i+1][j]) + arr[i][j]

for j in range(m-2, -1, -1):
    for i in range(n-2, -1, -1):
        dp_down[i][j] = max(dp_down[i+1][j], dp_down[i][j+1]) + arr[i][j]

ans = -int(1e9)
for i in range(n):
    for j in range(m):
        temp = dp_up[i][j]+dp_down[i][j]
        if ans < temp:
            ans = temp

print(ans)