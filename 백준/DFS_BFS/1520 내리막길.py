# 도착 지점까지 가는 경우의 수는 도착 지점이 아닌 임의의 점들에서
# 도착지점까지 가는 경우의 수를 합친 것과 같아짐

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(x, y):
    # 도착지점에 도달하면 1(한가지 경우의 수)를 리턴
    if x == m-1 and y == n-1:
        return 1

    # 이미 방문한 적이 있다면 그 위치에서 출발하는 경우의 수를 리턴
    if dp[x][y] != -1:
        return dp[x][y]

    temp = 0
    for w in range(4):
        nx, ny = x+dx[w], y+dy[w]
        if 0<=nx<m and 0<=ny<n:
            if arr[nx][ny] < arr[x][y]:
                temp += dfs(nx, ny)
    dp[x][y] = temp
    return dp[x][y]

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1]*n for _ in range(m)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

print(dfs(0,0))