from collections import deque
import sys
input = sys.stdin.readline
def bfs(x, cnt):
    q = deque([[x, cnt]])
    visit[x] = 1
    while q:
        t, cnt = q.popleft()
        if t == 100:
            return cnt
        dice = [t+1, t+2, t+3, t+4, t+5, t+6]
        for nt in dice:
            if 0<=nt<101 and visit[nt] == 0:
                if arr[nt]!=0:
                    q.append([arr[nt], cnt+1])
                else:
                    visit[nt] = 1
                    q.append([nt, cnt+1])

n, m = map(int, input().split())
arr = [0] *101
visit = [0]*101
for _ in range(n+m):
    s, e = map(int, input().split())
    arr[s]=e
print(bfs(1, 0))