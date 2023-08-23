from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, cnt):
    q = deque([(x, cnt)])
    # visit[x] = 1
    while q:
        w, cnt = q.popleft()
        if w == B:
            return cnt+1
        for k in ((2*w), (10*w+1)):
            if k < B+1:
                q.append((k, cnt+1))
    return -1

A, B = map(int, input().split())
# visit = [0]*(B+1)
print(bfs(A, 0))