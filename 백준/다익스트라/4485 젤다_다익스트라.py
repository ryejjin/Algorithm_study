import heapq

def dijkstra(x, y):
    heap = []
    D[x][y] = arr[x][y]
    heapq.heappush(heap, (D[x][y], x, y))

    while heap:
        d, x, y = heapq.heappop(heap)
        if visit[x][y]:continue
        visit[x][y]=1
        if x == n-1 and y==n-1:
            return D[n-1][n-1]

        for w in range(4):
            nx, ny = x+dx[w], y+dy[w]
            if 0<=nx<n and 0<=ny<n and visit[nx][ny]==0:
                if D[nx][ny] >= D[x][y]+arr[nx][ny]:
                    D[nx][ny] = D[x][y]+arr[nx][ny]
                    heapq.heappush(heap, (D[nx][ny], nx, ny))


tc = 0
while True:
    INF = int(1e9)
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    D = [[INF]*n for _ in range(n)]
    visit = [[0]*n for _ in range(n)]
    if n == 0:
        break
    else:
        tc += 1
        print(f'Problem {tc}: {dijkstra(0,0)}')