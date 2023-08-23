import sys
input = sys.stdin.readline

def dust():
    air = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if not (arr[i][j] == 0 or arr[i][j] == -1):
                cnt = 0
                for w in range(4):
                    ni = i + di[w]
                    nj = j + dj[w]
                    if 0 <= ni < r and 0 <= nj < c and arr[ni][nj] != -1:
                        cnt += 1
                        air[ni][nj] += arr[i][j] // 5
                air[i][j] -= ((arr[i][j] // 5) * cnt)

    for x in range(r):
        for y in range(c):
            arr[x][y] += air[x][y]
    return

def air_up(x, y):
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    dir = 0
    before = 0
    while True:
        nx = x + dx[dir]
        ny = y + dy[dir]
        if x == up and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >=c:
            dir += 1
            continue
        arr[x][y], before = before, arr[x][y]
        x, y = nx, ny
    return

def air_down(x, y):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    dir = 0
    before = 0
    while True:
        nx = x + dx[dir]
        ny = y + dy[dir]
        if x == down and y == 0:
            break
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            dir += 1
            continue
        arr[x][y], before = before, arr[x][y]
        x, y = nx, ny
    return

r, c, t = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(r)]

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

# [1] 공기 청정기 위치 찾기
up = down = 0
for i in range(r):
    if arr[i][0] == -1:
        up, down = i, i+1
        break

for _ in range(t):
    dust()
    air_up(up, 1)
    air_down(down, 1)

ans = 0
for k in range(r):
    for l in range(c):
        if arr[k][l] > 0:
            ans += arr[k][l]

print(ans)