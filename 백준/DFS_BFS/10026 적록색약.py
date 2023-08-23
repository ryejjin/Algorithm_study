from collections import deque

def bfs(s, e):
    q = deque()
    q.append([s,e])
    color[s][e] = 1
    while q:
        x, y = q.popleft()
        for w in range(4):
            nx = x + dx[w]
            ny = y + dy[w]
            if 0<=nx<n and 0<=ny<n and color[nx][ny]==0:
                if arr[x][y] == arr[nx][ny]:
                    color[nx][ny] = 1
                    q.append([nx, ny])



n = int(input())
arr = [list(input()) for _ in range(n)]
color = [[0]*n for _ in range(n)]
cnt = chk = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    for j in range(n):
        if color[i][j] == 0:
            bfs(i, j)
            cnt += 1

for k in range(n):
    for l in range(n):
        if arr[k][l] == 'G':
            arr[k][l] = 'R'

color = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if color[i][j] == 0:
            bfs(i, j)
            chk += 1
print(cnt, chk)