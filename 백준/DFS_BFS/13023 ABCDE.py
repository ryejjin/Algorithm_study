import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(x, cnt):
    global flag
    if cnt == 5 or flag == 1:
        flag = 1
        return
    visit[x] = True
    for i in graph[x]:
        if not visit[i]:
            dfs(x, cnt+1)
    visit[x] = False

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [False] * (n+1)
flag = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    dfs(i, 1)
    if flag:
        break

if flag:
    print(1)
else:
    print(0)