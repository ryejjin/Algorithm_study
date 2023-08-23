from collections import deque

def bfs(i, j):
    q = deque([[i, j]])
    arr[i][j] = 0
    cnt = 1
    while q:
        x, y = q.popleft()
        for w in range(4):
            nx, ny = x+dx[w], y+dy[w]
            if 0<=nx<m and 0<=ny<n and arr[nx][ny] ==1:
                cnt += 1
                arr[nx][ny] = 0
                q.append([nx, ny])
    count.append(cnt)

t = int(input())
for tc in range(t):
    m, n , k = map(int, input().split())
    arr = [[0]*n for _ in range(m)]
    for _ in range(k):
        s, e = map(int, input().split())
        arr[s][e] = 1
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    count = []
    for i in range(m):
        for j in range(n):
            if arr[i][j] == 1:
                bfs(i, j)
    print(len(count))