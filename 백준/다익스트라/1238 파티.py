# 목적지에서 출발지로 돌아가는 최단경로들은 일반적인 다익스트라로 풀고,
# 출발지에서 목적지로 가는 최단경로는 간선의 방향을 반대방향으로 하고 길을 찾아주는 다익스트라로 풀면 2번에 풀 수 있습니다.
import heapq
import sys
input = sys.stdin.readline

INF = int(1e8)
n, m, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s, e, t = map(int, input().split())
    graph[s].append([e, t])

def dijkstra(start):
    q = []
    distance = [INF] * (n+1)
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
    return distance

ans = 0
for i in range(1, n+1):
    go = dijkstra(i)
    back = dijkstra(x)
    ans = max(ans, go[x]+back[i])
print(ans)