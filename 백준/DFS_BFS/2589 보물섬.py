import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y):
    q = deque([(x, y)])
    visit[x][y] = 1
    dis = 0
    while q:
        i, j = q.popleft()
        for w in range(4):
            ni, nj = i+di[w], j+dj[w]
            if 0<=ni<n and 0<=nj<m:
                if not visit[ni][nj] and arr[ni][nj] =='L':
                    visit[ni][nj] = visit[i][j] + 1
                    q.append((ni, nj))
                    if dis < visit[ni][nj]:
                        dis = visit[ni][nj]
    return dis-1

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
max_dis = 0
for i in range(n):
    for j in range(m):
        visit = [[0]*m for _ in range(n)]
        if arr[i][j] == 'L':
            temp = bfs(i, j)
            if max_dis < temp:
                max_dis = temp

print(max_dis)