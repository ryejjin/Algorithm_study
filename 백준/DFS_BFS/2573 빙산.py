from collections import deque

def ice():
    melt = [[0]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if arr[x][y] != 0:
                temp = 0
                for w in range(4):
                    nx, ny = x+dx[w], y+dy[w]
                    if 0<=nx<n and 0<=ny<m and arr[nx][ny] == 0:
                        temp += 1
                melt[x][y] += temp

    for i in range(n):
        for j in range(m):
            arr[i][j] -= melt[i][j]
            if arr[i][j] < 0:
                arr[i][j] = 0

def bfs(k, l):
    q = deque()
    q.append([k, l])

    while q:
        x, y = q.popleft()
        for w in range(4):
            nx, ny = x+dx[w], y+dy[w]
            if 0<=nx<n and 0<=ny<m and arr[nx][ny]!=0 and visit[nx][ny] ==0:
                visit[nx][ny]=1
                q.append([nx,ny])

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

flag = 1
time = 0
while flag:
    cnt = 0
    zero = 0
    visit = [[0] * m for _ in range(n)]
    for k in range(n):
        for l in range(m):
            if arr[k][l]!=0 and visit[k][l]==0:
                bfs(k, l)
                cnt += 1
            if arr[k][l] == 0:
                zero += 1
    if cnt >= 2:
        flag = 0
        break
    if zero == (m*n):
        flag = 0
        time = 0
        break
    ice()
    time += 1

print(time)