n, m = map(int, input().split())
adj_lst = [[] for i in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    adj_lst[a].append(b)
    adj_lst[b].append(a)

visited = [False for i in range(n)]

def dfs(v, depth):
    global ans
    visited[v] = True
    if depth == 4:
        ans = True
        return
    for nxt in adj_lst[v]:
        if not visited[nxt]:
            dfs(nxt, depth+1)
            visited[nxt] = False

ans = False
for i in range(n):
    dfs(i,0)
    visited[i] = False
    if ans:
        break
if ans:
    print(1)
else:
    print(0)