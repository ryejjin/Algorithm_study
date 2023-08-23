import sys
input = sys.stdin.readline
from collections import deque

def bfs(x, y, z):
    q = deque([(x, y)])
    while q:
        i, j = q.popleft()
        visit[i][j] = 1
        for w in range(4):
            ni, nj = i+di[w], j+dj[w]
            if 0<=ni<m and 0<=nj<n:
                if arr[ni][nj] == z and visit[ni][nj] == 0:
                    visit[ni][nj] = visit[i][j] + 1
                    q.append((ni, nj))

n, m = map(int, input().split())
arr = [list(input()) for _ in range(m)]
White = []
Black = []
print(arr[0][0])
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

visit = [[0]*n for _ in range(m)]
for i in range(m):
    for j in range(n):
        if arr[m][n] == 'W' and visit[m][n] == 0:
            bfs(m, n, 'W')
        elif arr[m][n] == 'B' and visit[m][n] == 0:
            bfs(m, n, 'B')

print(visit)