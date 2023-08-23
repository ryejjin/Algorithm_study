n, m = map(int, input().split())
nemmo = [[0]*(m+1) for _ in range(n+1)]

ans = 0

def nemonemo(x, y):
    global ans
    if x == n+1 and y == 1:
        ans += 1
        return

    if x == m:
        ny = y+1
        nx = 1
    else:
        nx = x
        ny = y + 1

    if nemmo[x-1][y]==0 and nemmo[x][y-1]==0 and nemmo[x-1][y-1]==0:
        nemmo[x][y] = 1
        nemonemo(nx, ny)
        nemmo[x][y] = 0
    nemonemo(nx, ny)

nemonemo(1, 1)
print(ans)