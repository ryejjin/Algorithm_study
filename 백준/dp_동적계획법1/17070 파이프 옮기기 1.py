def dfs(x, y, dir):
    global ans
    if x == n-1 and y == n-1:
        ans += 1
        return

    # 대각선 방향 탐색
    if x+1 < n and y+1 < n and arr[x][y+1] == 0 and arr[x+1][y]==0 and arr[x+1][y+1]==0:
        dfs(x+1, y+1, 1)

    # 가로방향 탐색
    if (dir == 0 or dir == 1) and y+1<n and arr[x][y+1] == 0:
        dfs(x, y+1, 0)

    # 세로방향 탐색
    if (dir == 2 or dir == 1) and x+1<n and arr[x+1][y] == 0:
        dfs(x+1, y, 2)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
# 0 은 가로, 1은 대각선, 2는 세로
dfs(0, 1, 0)
print(ans)