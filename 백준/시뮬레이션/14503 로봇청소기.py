def robot(r, c, d):
    global cnt
    # 청소 시작점
    if arr[r][c] == 0:
        arr[r][c] = 9
        cnt += 1
    # 4방향 탐색
    for _ in range(4):
        d = (d + 3) % 4
        nr = r + dr[d]
        nc = c + dc[d]
        if 0<=nr<n and 0<=nc<m:
            if arr[nr][nc] == 0:
                r, c = nr, nc
                robot(r, c, d)
    else:
        if arr[r-dr[d]][c-dc[d]] == 1:
            return cnt

n, m = map(int, input().split())
r, c, d = map(int, input().split())
# arr이 1이면 벽이 있는 상태, 0이면 청소되지 않은 상태
arr = [list(map(int, input().split())) for _ in range(n)]
# d가 0이면 북/ 1이면 동/ 2이면 남/ 3이면 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cnt = 0

robot(r, c, d)
print(cnt)