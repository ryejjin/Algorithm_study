from collections import deque

def bfs():
    while q:
        x, y = q.popleft()
        for w in range(4):
            nx = x + dx[w]
            ny = y + dy[w]
            if 0<=nx<n and 0<=ny<m and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y]+1
                q.append([nx, ny])

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
q = deque([])
anw = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append([i, j])
bfs()

for k in arr:
    for l in k:
        if l == 0:
            print(-1)
            exit()
    anw = max(anw, max(k))
print(anw-1)