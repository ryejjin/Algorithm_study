import heapq

INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append([e,w])
    graph[e].append([s,w])

def dijkstra(start):
    q = []
    distance = [INF] * (n + 1)
    heapq.heappush(q, (0, start))
    distance[start]=0
    p = [0] * (n+1)
    while q:
        dist, now = heapq.heappop(q)

        if distance[now]<dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                p[i[0]] = now
                heapq.heappush(q, (cost, i[0]))
    return p[1:]
temp = []
for i in range(1, n+1):
    temp.append(dijkstra(i))

ans = list(map(list, zip(*temp)))

for i in range(n):
    for j in range(n):
        if ans[i][j]==0:
            ans[i][j]='-'

for k in ans:
    print(*k, end=' ')
    print()