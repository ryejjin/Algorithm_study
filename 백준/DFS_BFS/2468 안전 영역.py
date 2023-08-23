from collections import deque

def bfs(s, e, a):
    q = deque()
    q.append([s,e])
    visited[s][e] = 1
    while q:
        x, y = q.popleft()
        for w in range(4):
            nx = x + dx[w]
            ny = y + dy[w]
            if 0<=nx<n and 0<=ny<n:
                if arr[nx][ny] > a and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx, ny])


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
_max = 0
result = 0
ans = []
for i in range(n):
    for j in range(n):
        if arr[i][j] > _max:
            _max = arr[i][j]

for a in range(_max):
    visited = [[0] * (n + 1) for _ in range(n + 1)]
    cnt = 0
    for k in range(n):
        for l in range(n):
            if arr[k][l] > a and visited[k][l] == 0:
                bfs(k, l, a)
                cnt += 1
    result = max(result, cnt)
print(result)