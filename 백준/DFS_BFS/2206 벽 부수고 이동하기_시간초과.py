from collections import deque
import sys
input = sys.stdin.readline
def bfs(i, j):
    global _min
    q = deque([[i,j]])
    v[i][j] = 1
    while q:
        x, y = q.popleft()
        for w in range(4):
            nx, ny = x+dx[w], y+dy[w]
            if 0<=nx<n and 0<=ny<m:
                if arr[nx][ny] == '0' and v[nx][ny] == 0:
                    q.append([nx,ny])
                    v[nx][ny] = v[x][y] + 1
                    if v[nx][ny] > _min:
                        return
    if v[-1][-1] != 0 and v[-1][-1] <_min :
        _min = v[-1][-1]
    return _min


n, m = map(int, input().split())
arr = [list(map(str,input())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
_min = 10e6
v = [[0] * m for _ in range(n)]
bfs(0,0)
for i in range(n):
    for j in range(m):
        if arr[i][j] == '1':
            arr[i][j] = '0'
            v = [[0] * m for _ in range(n)]
            bfs(0,0)
            arr[i][j] = '1'

if _min == 10e6:
    print(-1)
else:
    print(_min)