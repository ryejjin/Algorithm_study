from collections import deque
import sys
input = sys.stdin.readline

def bfs(r):
    q = deque([r])
    cnt = 1
    visit[r] = cnt
    while q:
        t = q.popleft()
        for w in graph[t]:
            if not visit[w]:
                cnt += 1
                visit[w] = cnt
                q.append(w)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [0]*(n+1)
for _ in range(m):
    s, e = map(int, input().split())
    graph[s].append(e)
    graph[e].append(s)

for i in graph:
    i.sort()    # bfs1
for i in graph:
    i.sort(reverse=True)    #bfs2

bfs(r)
for j in visit[1:]:
    print(j)