from collections import deque
import sys
input = sys.stdin.readline

def bfs(x):
    q = deque()
    q.append(x)
    visit[x] = 1
    while q:
        t = q.popleft()
        ans.append(t)
        for w in graph[t]:
            if visit[w] == 0:
                visit[w] = 1
                q.append(w)

n = int(input())
graph = [[] for _ in range(n+1)]
visit = [0] * (n+1)
for _ in range(n-1):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)
order = list(map(int, input().split()))
ans = []
for k in range(n+1):
    graph[k].sort(key=lambda x : order.index(x))
bfs(1)

if order == ans:
    print(1)
else:
    print(0)