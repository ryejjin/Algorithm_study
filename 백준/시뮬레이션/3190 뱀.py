from collections import deque
import sys
input = sys.stdin.readline

def apple_snake(x):
    global i, j, dir, time, flag
    cnt = time
    while cnt < x:
        cnt += 1
        time += 1
        ri, rj = rotate[dir]
        ni, nj = i + ri, j + rj
        if 0 <= ni < N and 0 <= nj < N:
            if arr[ni][nj] == 4:
                arr[ni][nj] = 9
            elif arr[ni][nj] == 9:
                flag = 1
                return
            else:
                di, dj = snake.popleft()
                arr[di][dj] = 0
            snake.append([ni, nj])
            arr[ni][nj] = 9
            i, j = ni, nj
        else:
            flag = 1
            return
    if C == 'D':
        dir = (dir + 1) % 4
    else:
        dir = (dir + 3) % 4

# 사과는 4, 뱀은 9
N = int(input())
K = int(input())
arr = [[0]*N for _ in range(N)]
arr[0][0]=9
# 사과 배치
for _ in range(K):
    col, row = map(int, input().split())
    arr[col-1][row-1] = 4

rotate = [(0,1), (1,0), (0,-1), (-1,0)]

# 뱀이 위치한 좌표를 큐에 넣어서 접근?
L = int(input())
snake = deque([[0, 0]])
i = j = dir = time = flag = 0

for _ in range(L):
    X, C = map(str, input().split())
    x = int(X)
    apple_snake(x)
    if flag == 1:
        print(time)
        break
else:
    apple_snake(10000)
    if flag == 1:
        print(time)