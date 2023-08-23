import sys
from collections import deque
input = sys.stdin.readline

def BFS(v):
    visit = [0]*(N+1)
    visit[v] = 1
    res = 0
    q = deque([(v, int(1e9))])

    while q:
        v, usado = q.pop()
        for v_next, u_next in graph[v]:
            u_next = min(usado, u_next)
            if u_next >= k and not visit[v_next]:
                res += 1
                q.append((v_next, u_next))
                visit[v_next]=1
    return res

N, Q = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    p, q, r = map(int, input().split())
    graph[p].append([q, r])
    graph[q].append([p, r])

for _ in range(Q):
    k, v = map(int, input().split())
    print(BFS(v))