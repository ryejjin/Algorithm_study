import sys
input = sys.stdin.readline

def dfs(x):
    stack = [x]
    cnt = 1
    visit[x] = cnt
    while stack:
        t = stack.pop()
        if not visit[t]:
            cnt += 1
            visit[t] = cnt
        for w in graph[t]:
            if visit[w] == 0:
                stack.append(w)


n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [0]*(n+1)
for _ in range(m):
    u, v = map(int, input().split())
    if len(graph[u])==0:
        graph[u].append(v)
    else:
        graph[u].append(v)
    if len(graph[v]) == 0:
        graph[v].append(u)
    else:
        graph[v].append(u)
for i in graph:
    i.sort()                # DFS2
for i in graph:
    i.sort(reverse=True)    # DFS1
dfs(r)

for j in range(1,n+1):
    print(visit[j])