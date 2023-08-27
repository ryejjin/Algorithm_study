import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(i, j):
    if i<0 or i>=n or j<0 or j>=m:
        return 1
    if visit[i][j]:
        return visit[i][j]

    visit[i][j] = -1
    di, dj = dict[arr[i][j]]
    visit[i][j] = dfs(i+di, j+dj)
    return visit[i][j]

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
dict = {'U':(-1, 0), 'R':(0, 1), 'D':(1, 0), 'L':(0, -1)}

ans = 0

visit = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if not visit[i][j] and dfs(i, j) == 1:
            ans += 1
        elif visit[i][j] == 1:
            ans += 1

print(ans)