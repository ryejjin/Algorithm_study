c, r = map(int, input().split())
k = int(input())
#우하좌상
di = [0, 1, 0 ,-1]
dj = [1, 0, -1, 0]
arr = [[0] * r for _ in range(c)]
i = j = dr = 0
for num in range(1, c*r+1):
    arr[i][j] = num
    ni = i + di[dr]
    nj = j + dj[dr]
    if 0 <= ni < c and 0<= nj < r and arr[ni][nj] == 0:
        i, j = ni, nj
    else:
        dr = (dr+1) % 4
        i, j = i + di[dr], j + dj[dr]

s = e = 0
flag = 0
for i in range(c):
    for j in range(r):
        if arr[i][j] == k:
            s, e = i+1, j+1
            flag = 1
if flag:
    print(s, e)
else:
    print(0)