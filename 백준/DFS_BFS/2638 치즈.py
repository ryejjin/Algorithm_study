from collections import deque

def find_air(i, j):
    q = deque([[i, j]])
    air[i][j] = 2

    while q:
        ci, cj = q.popleft()
        for w in range(4):
            ni, nj = ci+di[w], cj+dj[w]
            if 0<=ni<n and 0<=nj<m:
                if air[ni][nj] == 0 and arr[ni][nj]==0:
                    air[ni][nj] = 2
                    q.append([ni, nj])

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

cnt = 0
flag = 1
while flag:
    air = [[0] * m for _ in range(n)]
    one = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                find_air(i, j)
                break
    for k in range(n):
        for l in range(m):
            temp = 0
            if arr[k][l] == 1:
                one += 1
                for w in range(4):
                    nk, nl = k+di[w], l+dj[w]
                    if 0<=nk<n and 0<=nl<m and air[nk][nl] == 2:
                        temp += 1
            if temp >= 2:
                arr[k][l] = 0
    cnt += 1
    if one == 0:
        flag = 0
        break
print(cnt-1)