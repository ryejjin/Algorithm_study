import sys
sys.setrecursionlimit(10**6)

def dfs(n, graph, visit):
    if visit[n] == 1:
        return
    else:
        visit[n] = 1
        for x in graph[n]:
            dfs(x, graph, visit)
    return

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
graphR = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graphR[y].append(x)
s, t = map(int, input().split())

fromS = [0]*(n+1)
fromS[t] = 1
dfs(s, graph, fromS)

fromT = [0]*(n+1)
fromT[s] = 1
dfs(t, graph, fromT)

toS = [0]*(n+1)
dfs(s, graphR, toS)

toT = [0]*(n+1)
dfs(s, graphR, toT)

cnt = 0
for i in range(1, n+1):
    if fromS[i] and fromT[i] and toS[i] and toT[i]:
        cnt += 1

print(cnt-2)