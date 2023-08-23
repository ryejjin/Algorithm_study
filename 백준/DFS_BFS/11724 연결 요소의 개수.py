import sys
input = sys.stdin.readline
from collections import deque

def bfs(x):
    q = deque([x])

    while q:
        t = q.popleft()
        visit[t] = 1

        for w in graph[t]:
            if visit[w] == 0:
                visit[w] = 1
                q.append(w)


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

cnt = 0
visit = [0]*(n+1)
for i in range(1, n+1):
    if visit[i] == 0:
        bfs(i)
        cnt += 1

print(cnt)