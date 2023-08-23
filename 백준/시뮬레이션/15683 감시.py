def one(x, y):
    graph[x][y] = 1
    temp = 0
    dir = 0


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
graph = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            one(i, j)