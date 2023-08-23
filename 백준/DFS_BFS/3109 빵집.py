import sys
input = sys.stdin.readline

def DFS(s, e):
    global cnt
    visit[s][e] = 1
    for ds, de in dir:
        ns, ne = s+ds, e+de
        if 0<=ns<R and 0<=ne<C:
            if ne == C-1:
                cnt += 1
                return True
            if visit[ns][ne]==0 and pipe[ns][ne] == '.':
                visit[ns][ne] = 1
                if DFS(ns, ne):
                    return True
    return False

R, C = map(int, input().split())
pipe = [input() for _ in range(R)]
visit = [[0]*C for _ in range(R)]

dir = [(-1, 1), (0, 1), (1, 1)]
cnt = 0
for i in range(R):
    DFS(i, 0)

print(cnt)