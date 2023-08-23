import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

def bfs(k):
    q = deque([k])
    cnt = 0
    while q:
        p = q.popleft()
        visit[p] = 1
        cnt += 1
        for w in graph[p]:
            if visit[w] == 0:
                visit[w] = 1
                q.append(w)
    return cnt

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

ans = [0]*(n+1)

for i in range(1, n+1):
    visit = [0]*(n+1)
    ans[i] = bfs(i)

_max = max(ans)
for i in range(1, n+1):
    if _max == ans[i]:
        print(i, end = ' ')