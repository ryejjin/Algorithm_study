import heapq, sys
input = sys.stdin.readline

INF = int(1e9)
n = int(input())
graph = [list(input()) for _ in range(n)]
D = [[INF]*n for _ in range(n)]
visit = [[0]*n for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dijkstra(x, y):
    q = []
    D[x][y] = 0
    heapq.heappush(q, (D[x][y], x, y))
    while q:
        dis, x, y = heapq.heappop(q)

        if x == n-1 and y == n-1:
            return

        for w in range(4):
            nx, ny = x+dx[w], y+dy[w]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == '0' and D[nx][ny] > D[x][y]+1:
                    D[nx][ny] = D[x][y]+1
                    heapq.heappush(q, (D[nx][ny], nx, ny))
                elif graph[nx][ny] == '1' and D[nx][ny] > D[x][y]:
                    D[nx][ny] = D[x][y]
                    heapq.heappush(q, (D[nx][ny], nx, ny))

dijkstra(0,0)


print(D[n-1][n-1])