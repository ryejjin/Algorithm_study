from collections import deque

def bfs():
    while q:
        x, y, z = q.popleft()
        for w in range(6):
            nx, ny, nz = x+dx[w], y+dy[w], z+dz[w]
            if 0<=nx<h and 0<=ny<n and 0<=nz<m:
                if tomato[nx][ny][nz] == 0:
                    tomato[nx][ny][nz] = tomato[x][y][z]+1
                    q.append([nx, ny, nz])


m, n, h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
ans = 0
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

q = deque([])
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                q.append([i, j, k])
bfs()

for a in tomato:
    for b in a:
        for c in b:
            if c == 0:
                print(-1)
                exit()
        ans = max(ans, max(b))
print(ans-1)