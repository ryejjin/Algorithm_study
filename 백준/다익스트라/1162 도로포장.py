# cnt라는 차원을 더해서 cnt가 증가했을 때 다익스트라를 구함
import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)
n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [[INF] * (k+1) for _ in range(n+1)]
for _ in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((w,e))
    graph[e].append((w,s))

def dijkstra(start):
    q = []
    cnt = 0
    heapq.heappush(q,(0, start, cnt))
    distance[start][cnt] = 0
    while q:
        wei, now, cnt = heapq.heappop(q)
        if distance[now][cnt] < wei:
            continue
        for val, next in graph[now]:
            n_wei = val + wei
            if distance[next][cnt] > n_wei:
                distance[next][cnt] = n_wei
                heapq.heappush(q, (n_wei, next, cnt))

            if cnt < k and distance[next][cnt+1] > wei:
                distance[next][cnt+1] = wei
                heapq.heappush(q, (wei, next, cnt+1))

dijkstra(1)
print(min(distance[n]))