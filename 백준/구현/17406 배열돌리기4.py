import sys
input = sys.stdin.readline

def perm(N, k):
    if N == k:
        Narr = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                Narr[i][j] = arr[i][j]
        rotate(order, Narr)
        find_min(Narr)

    else:
        for i in range(N):
            if visit[i] == 0:
                visit[i] = 1
                order[k] = A[i]
                perm(N, k+1)
                visit[i] = 0

# 배열 회전 함수
def rotate(lst, Narr):
    for idx in lst:
        r, c, s = info[idx]
        x1, y1 = r-s-1, c-s-1
        x2, y2 = r+s-1, c+s-1

        while True:
            if x1>=x2 or y1>=y2:
                break
            dir = 0
            x, y, before = x1, y1, Narr[x1][y1]
            while True:
                nx = x + dx[dir]
                ny = y + dy[dir]
                if not x1 <= nx <= x2 or not y1<=ny<=y2:
                    dir += 1
                    continue
                temp = Narr[nx][ny]
                Narr[nx][ny] = before
                before = temp
                x, y = nx, ny
                if (x, y) == (x1, y1):
                    x1+=1; y1+=1; x2-=1; y2-=1
                    break

# 행의 합 중 최솟값 찾기
def find_min(Narr):
    global res
    for i in range(n):
        temp = 0
        for j in range(m):
            temp += Narr[i][j]
        if res > temp:
            res = temp

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
info = [list(map(int, input().split())) for _ in range(k)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

res = int(1e9)

# 배열 돌리는 순서 idx 구하기
A = [ i for i in range(k)]
order = [0] * k
visit = [0] * k
perm(k, 0)

print(res)