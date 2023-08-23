# 3차원 행렬로 벽을 부쉈을 때 이동거리와 안부쉈을때 이동거리를 저장
def bfs(x, y, z):
    q = deque()
    q.append((x, y, z))
    while q:
        a, b, c = q.popleft()
        if a == n-1 and b == m-1:
            return visited[a][b][c]
        for w in range(4):
            nx, ny = a+dx[w], b+dy[w]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] == 1 and c == 0:
                visited[nx][ny][1] = visited[a][b][0] + 1
                q.append((nx, ny, 1))
            elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[a][b][c] + 1
                q.append((nx, ny, c))
    return -1

from collections import deque

n, m = map(int, input().split())
graph = []

visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

for i in range(n):
    graph.append(list(map(int, input())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

print(bfs(0,0,0))