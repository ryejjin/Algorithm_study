import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    q = deque(vir)
    time = 0
    while q:
        if time == s:
            break
        for _ in range(len(q)):
            virus, i, j = q.popleft()
            for w in range(4):
                ni, nj = i+di[w], j+dj[w]
                if 0<=ni<n and 0<=nj<n:
                    if arr[ni][nj] == 0:
                        arr[ni][nj] = virus
                        q.append((virus, ni, nj))
        time += 1

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

vir = []
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            vir.append((arr[i][j], i, j))
vir.sort()
bfs()

print(arr[x-1][y-1])