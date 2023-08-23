from collections import deque

def bfs(s, e):
    q = deque()
    q.append([s,e])
    arr[s][e] = '0'
    cnt = 1
    while q:
        x, y = q.popleft()
        for w in range(4):
            nx = x+dx[w]
            ny = y+dy[w]
            if 0<=nx<n and 0<=ny<n:
                if arr[nx][ny] == '1':
                    cnt += 1
                    arr[nx][ny] = '0'
                    q.append([nx,ny])
    count.append(cnt)

n = int(input())
arr = [list(input()) for _ in range(n)]
count = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    for j in range(n):
        if arr[i][j] == '1':
           bfs(i, j)
count.sort()
print(len(count))
for k in count:
    print(k)