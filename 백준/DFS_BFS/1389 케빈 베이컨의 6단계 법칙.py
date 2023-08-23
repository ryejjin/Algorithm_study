import sys
input = sys.stdin.readline
from collections import deque

def bfs(x):
    q = deque([x])
    while q:
        k = q.popleft()
        for w in graph[k]:
            if visit[w] == 0:
                visit[w] = visit[k]+1
                q.append(w)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = [0]*(n+1)

for i in range(1, n+1):
    visit = [0]*(n+1)
    bfs(i)
    for j in range(1, n+1):
        if j !=i:
            ans[i]+=visit[j]

_min = int(1e9)
idx = 0
for x in range(1, n+1):
    if _min>ans[x]:
        _min = ans[x]
        idx = x

print(idx)