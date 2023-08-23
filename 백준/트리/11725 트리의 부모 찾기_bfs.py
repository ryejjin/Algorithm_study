from collections import deque

def bfs(matrix, i, visited):
    q = deque()
    q.append(i)
    visited[i] = True
    while q:
        v = q.popleft()
        for i in matrix[v]:
            if not visited[i]:
                anw[i] = v
                q.append(i)
                visited[i] = True

n = int(input())
matrix = [[]*(n+1) for _ in range(n+1)]
anw = [0] * (n+1)
visited = [False] * (n+1)
for _ in range(n-1):
    p, c = map(int, input().split())
    matrix[p].append(c)
    matrix[c].append(p)

bfs(matrix, 1, visited)
for i in range(2, n+1):
    print(anw[i])