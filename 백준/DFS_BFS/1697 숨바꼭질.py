from collections import deque

def bfs(n):
    q = deque()
    q.append(n)

    while q:
        t = q.popleft()
        if t == k:
            return
        cal = [t-1, t+1, 2*t]
        for nt in cal:
            if 0<= nt <= 1000001 and visit[nt]==0:
                visit[nt] = visit[t] + 1
                q.append(nt)

n, k = map(int, input().split())
time = 0
visit = [0]*(10000001)
bfs(n)
print(visit[k])