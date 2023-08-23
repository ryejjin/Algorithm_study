import heapq

def dijkstra(x):
    q = []
    heapq.heappush(q,[0, x])
    distance[x] = 0
    while q:
        dist, now = heapq.heappop(q)

        if dist < distance[now]:
            continue

        for i in graph[now]:
            cost = dist+i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, [cost, i[0]])


INF = int(1e9)
v, e = map(int, input().split())
k = int(input())
graph = [[]for _ in range(v+1)]
distance = [INF]*(v+1)
for _ in range(e):
    s, e, w = map(int, input().split())
    graph[s].append([e, w])

dijkstra(k)

for j in range(1, v+1):
    if distance[j] != INF:
        print(distance[j])
    else:
        print('INF')