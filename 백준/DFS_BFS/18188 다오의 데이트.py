import sys
input = sys.stdin.readline
from collections import deque

def dao(s, e):
    q = deque([[s, e, '', 0]])
    while q:
        s, e, m, k = q.popleft()
        if arr[s][e] == 'Z':
            ans.append(m)
        if k < n:
            x, y = move[k]
            if x == 'W' or y=='W':
                ns, ne = s-1, e
                if 0<=ns<h and 0<=ne<w:
                    if arr[ns][ne] == '.':
                        q.append([ns, ne, m+'W', k+1])
                    if arr[ns][ne] == 'Z' or arr[ns][ne]=='D':
                        q.append([ns, ne, m+'W', k+1])

            if x == 'A' or y=='A':
                ns, ne = s, e-1
                if 0<=ns<h and 0<=ne<w:
                    if arr[ns][ne] == '.':
                        q.append([ns, ne, m+'A', k+1])
                    if arr[ns][ne] == 'Z' or arr[ns][ne]=='D':
                        q.append([ns, ne, m+'A', k+1])

            if x == 'S' or y == 'S':
                ns, ne = s + 1, e
                if 0 <= ns < h and 0 <= ne < w:
                    if arr[ns][ne] == '.':
                        q.append([ns, ne, m+'S', k+1])
                    if arr[ns][ne] == 'Z' or arr[ns][ne]=='D':
                        q.append([ns, ne, m+'S', k+1])

            if x == 'D' or y == 'D':
                ns, ne = s, e + 1
                if 0 <= ns < h and 0 <= ne < w:
                    if arr[ns][ne] == '.':
                        q.append([ns, ne, m+'D', k+1])
                    if arr[ns][ne] == 'Z' or arr[ns][ne]=='D':
                        q.append([ns, ne, m+'D', k+1])

h, w = map(int, input().split())
arr = [list(input()) for _ in range(h)]
# 다오의 위치
s, e = 0, 0
ans = []

for i in range(h):
    for j in range(w):
        if arr[i][j] == 'D':
            s, e = i, j

n = int(input())
move = [list(input().split()) for _ in range(n)]
dao(s, e)
# print(ans)
if ans:
    print('YES')
    print(ans[0])
else:
    print('NO')