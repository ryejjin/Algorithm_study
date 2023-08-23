import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(x, y, cursum):
    global ans
    if ans <= cursum:
        return
    if x == n-1 and y == n-1:
        if ans > cursum:
            ans = cursum
    for w in range(4):
        nx, ny = x+dx[w], y+dy[w]
        if 0<=nx<n and 0<=ny<n and visit[nx][ny] == 0:
            visit[nx][ny] =1
            dfs(nx, ny, cursum+arr[nx][ny])
            visit[nx][ny] = 0

tc = 0
while True:
    n = int(input())
    if n != 0:
        tc += 1
        arr = [list(map(int, input().split())) for _ in range(n)]
        visit = [[0]*n for _ in range(n)]
        visit[0][0] = 1
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        ans = 1e9
        dfs(0,0,arr[0][0])
        print(f'Problem {tc}: {ans}')
    else:
        break