from collections import deque

def bfs(ci, cj, cnt):
    q = deque([[ci, cj, cnt]])
    arr[ci][cj] = 1
    while q:
        x, y, cnt = q.popleft()
        if x == di and y == dj:
            return cnt
        else:
            for (dx, dy) in ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1)):
                nx, ny = x+dx, y+dy
                if 0<=nx<i and 0<=ny<i and arr[nx][ny] == 0:
                    arr[nx][ny] = 1
                    q.append([nx, ny, cnt+1])

t = int(input())
for tc in range(t):
    i = int(input())    # 체스판 한 변의 길이
    ci, cj = map(int, input().split())
    di, dj = map(int, input().split())
    arr = [[0]*i for _ in range(i)]
    cnt = 0
    print(bfs(ci, cj, cnt))