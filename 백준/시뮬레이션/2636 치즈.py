from collections import deque
def bfs(x, y):
    q = deque([[x,y]])
    air[x][y] = 2
    while q:
        i, j = q.popleft()
        for w in range(4):
            ni, nj = i+di[w], j+dj[w]
            if 0<=ni<n and 0<=nj<m:
                if arr[ni][nj] == 0 and air[ni][nj] == 0:
                    air[ni][nj] = 2
                    q.append([ni,nj])

def cheeze():
    chz = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                chz += 1
                for w in range(4):
                    ni, nj = i+di[w], j+dj[w]
                    if 0<=ni<n and 0<=nj<m:
                        if air[ni][nj] == 2:
                            arr[i][j] = 0
    return chz

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

time = 0
ans = []
flag = 1
while flag:
    air = [[0]*m for _ in range(n)]
    time += 1
    bfs(0,0)
    ans.append(cheeze())
    if ans[-1] == 0:
        flag = 0
        break

print(time-1)
print(ans[-2])
