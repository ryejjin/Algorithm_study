# 0은 단위 도로가 이미 존재하는 것
# 1은 단위도로가 없고 1의 비용으로 도로 건설
# 2는 단위 도로가 없고 2의 비용으로 도로를 건설
# -1은 도로 건설 불가

import heapq
INF = int(1e9)
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]

if graph[0][0] == -1:
    print(-1)
    exit()

D = [[INF]*n for _ in range(m)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dijkstra(x, y):
    heap = []
    D[x][y] = graph[x][y]
    heapq.heappush(heap, (D[x][y], x, y))
    while heap:
        d, x, y = heapq.heappop(heap)

        if D[x][y] < d:
            continue

        for w in range(4):
            nx, ny = x+dx[w], y+dy[w]
            if 0<=nx<m and 0<=ny<n:
                if graph[nx][ny] != -1:
                    if D[nx][ny] > D[x][y] + graph[nx][ny]:
                        D[nx][ny] = D[x][y] + graph[nx][ny]
                        heapq.heappush(heap, (D[nx][ny], nx, ny))
    return -1

dijkstra(0,0)

if D[m-1][n-1] == INF:
    print(-1)
else:
    print(D[m-1][n-1])