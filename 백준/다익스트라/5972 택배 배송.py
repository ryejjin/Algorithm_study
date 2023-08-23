import heapq

def dijkstra(start):
    q=[]
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

INF = int(1e9)
n, m = map(int, input().split())
graph = [[]for _ in range(n+1)]
distance = [INF]*(n+1)
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append([e, w])
    graph[e].append([s, w])

dijkstra(1)

print(distance[-1])