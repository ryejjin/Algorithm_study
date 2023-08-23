import sys
from collections import deque
input = sys.stdin.readline

def bfs(n):
    q = deque([n])
    visit[n] = 0

    while q:
        t = q.popleft()

        if t == k:
            return

        for x in ((2*t), (t+1), (t-1)):
            if 0<=x<100001 and visit[x] == -1:
                if x == 2*t:
                    visit[x] = visit[t]
                    q.appendleft(x)
                else:
                    visit[x] = visit[t]+1
                    q.append(x)

n, k = map(int, input().split())
visit = [-1]*100001
bfs(n)
print(visit[k])