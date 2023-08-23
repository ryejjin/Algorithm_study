def bfs(v):
    visited = [0] * (t+1)
    q = [v]
    visited[v] = 1
    while q:
        x = q.pop(0)
        for w in adjL[x]:
            if not visited[w]:
                virus.append(w)
                q.append(w)
                visited[w] = visited[x] + 1



t = int(input())
n = int(input())
adjL = [[] * (t+1) for _ in range(t+1)]
for _ in range(n):
    p, c = map(int, input().split())
    adjL[p].append(c)
    adjL[c].append(p)
virus = []
bfs(1)
print(len(virus))