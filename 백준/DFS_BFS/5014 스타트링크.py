from collections import deque

def bfs(x):
    q = deque()
    q.append(x)
    visit[x] = 1
    while q:
        t = q.popleft()
        if t == g:
            return
        cal = [t+u, t-d]
        for nt in cal:
            if 0 < nt <= f and visit[nt]==0:
                visit[nt] = visit[t]+1
                q.append(nt)

f, s, g, u, d = map(int, input().split())
visit = [0] * 10000001
bfs(s)
if s == g:
    print(0)
elif visit[g]==0:
    print('use the stairs')
else:
    print(visit[g]-1)