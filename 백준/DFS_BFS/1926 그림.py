from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    global res, temp
    q = deque([[x, y]])
    visit[x][y] = 1
    while q:
        i, j = q.popleft()
        if arr[i][j] == 1:
            temp += 1
            if temp > res:
                res = temp
        for w in range(4):
            ni, nj = i+di[w], j+dj[w]
            if 0<=ni<n and 0<=nj<m:
                if arr[ni][nj] == 1 and visit[ni][nj] == 0:
                    visit[ni][nj] = 1
                    q.append([ni, nj])

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]
visit = [[0]*m for _ in range(n)]

res = 0
cnt = 0
for i in range(n):
    for j in range(m):
        temp = 0
        if arr[i][j] == 1 and visit[i][j] == 0:
            bfs(i, j)
            cnt += 1

print(cnt)
print(res)