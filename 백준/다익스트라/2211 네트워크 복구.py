import heapq, sys
input = sys.stdin.readline

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    D[start]=0

    while q:
        dist, now = heapq.heappop(q)

        if D[now] < dist: continue

        for next_node, next_val in graph[now]:
            cost = dist + next_val
            if D[next_node] > cost:
                D[next_node] = cost
                parent[next_node] = now
                heapq.heappush(q, (cost, next_node))


INF = int(1e9)
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
D = [INF] * (n+1)
parent = [0] * (n+1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

dijkstra(1)

print(n-1)
for i in range(2, n+1):
    print(i, parent[i])