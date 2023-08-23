from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    global gram
    q = deque([(0, 0)])
    visit[0][0]=1
    while q:
        i, j = q.popleft()
        if i == N-1 and j == M-1:
            return min(gram, visit[i][j]-1)
        if arr[i][j] == 2:
            gram = (N-1-i)+(M-1-j)+visit[i][j]-1
        for w in range(4):
            ni, nj = i+di[w], j+dj[w]
            if 0<=ni<N and 0<=nj<M:
                if arr[ni][nj] != 1 and visit[ni][nj] == 0:
                    visit[ni][nj] = visit[i][j] + 1
                    q.append((ni, nj))
    return gram


N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[0]*M for _ in range(N)]
gram = int(1e9)

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

res = bfs()

if res > T:
    print('Fail')
else:
    print(res)