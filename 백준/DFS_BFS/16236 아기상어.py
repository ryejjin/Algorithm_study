import sys
from collections import deque
input = sys.stdin.readline

# 아기상어가 갈 수 있는 칸 찾기
def bfs(s, e, baby):
    dis = [[0]*n for _ in range(n)]
    visit = [[0]*n for _ in range(n)]
    q = deque([[s,e]])
    visit[s][e] = 1
    temp = []
    while q:
        x, y = q.popleft()
        for w in range(4):
            nx, ny = x+dx[w], y+dy[w]
            if 0<=nx<n and 0<=ny<n and visit[nx][ny] ==0:
                if arr[nx][ny] <= baby:
                    q.append([nx, ny])
                    visit[nx][ny] = 1
                    dis[nx][ny] = dis[x][y] + 1
                    if arr[nx][ny] < baby and arr[nx][ny] != 0:
                        temp.append((nx, ny, dis[nx][ny]))
    return sorted(temp, key=lambda x : (-x[2], -x[0], -x[1]))

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
x, y, baby = 0, 0, 2

# 아기상어가 있는 위치
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            x, y = i, j

cnt = 0     # 아기상어의 크기만큼 먹이를 먹는지
result = 0  # 엄마상어한테 도움을 요청할때까지의 시간

while True:
    fish = bfs(x, y, baby)
    # 더 이상 먹을 수 있는 물고기가 공간에 없다면 종료
    if len(fish) == 0:
        break

    nx, ny, dist = fish.pop()

    result += dist
    arr[x][y], arr[nx][ny] = 0, 0

    x, y = nx, ny
    cnt += 1
    if cnt == baby:
        baby += 1
        cnt = 0
print(result)