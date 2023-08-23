dir = {1:(-1, 0), 2:(-1, -1), 3:(0, -1), 4:(1,-1), 5:(1, 0), 6:(1,1), 7:(0,1), 8:(-1, 1)}

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
cloud = [(n-1,0), (n-1,1), (n-2,0), (n-2,1)]
for _ in range(m):
    move = []
    d, s = map(int, input().split())
    dy, dx = dir[d]
    for x, y in cloud:
        nx = (x + dx*s)%n
        ny = (y + dy*s)%n
        arr[nx][ny] += 1
        move.append((nx, ny))

    for x, y in move:
        for tx, ty in ((-1,-1), (-1, 1), (1, -1), (1, 1)):
            wx, wy = x+tx, y+ty
            if 0<=wx<n and 0<=wy<n and arr[wx][wy] > 0:
                arr[x][y] += 1

    new = []
    for i in range(n):
        for j in range(n):
            if (i, j) not in move and arr[i][j] >= 2:
                arr[i][j] -= 2
                new.append((i, j))
    cloud = new

anw = 0
for i in range(n):
    for j in range(n):
        anw += arr[i][j]

print(anw)

