# 불을 먼저 모두 확산 시킨 후, 지훈이가 이동하는 경로가 불이 확산되기 전인지 후인지 확인

from collections import deque
def bfs():
    while fr:
        s, e = fr.popleft()
        for w in range(4):
            ns = s + ds[w]
            ne = e + de[w]
            if 0<=ns<r and 0<=ne<c:
                if not fire[ns][ne] and arr[ns][ne]!='#':
                    fire[ns][ne] = fire[s][e] + 1
                    fr.append([ns, ne])

    while jh:
        x, y = jh.popleft()
        for w in range(4):
            nx = x + ds[w]
            ny = y + de[w]
            if 0<=nx<r and 0<=ny<c:
                if not jihoon[nx][ny] and arr[nx][ny] != '#':
                    if not fire[nx][ny] or fire[nx][ny] > jihoon[x][y]+1:       # 지훈이가 한칸 갔을 때 불이 붙어져있는가?
                        jihoon[nx][ny] = jihoon[x][y]+1
                        jh.append([nx,ny])
            else:
                return jihoon[x][y]
    return 'IMPOSSIBLE'

r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]
jihoon = [[0]*c for _ in range(r)]
fire = [[0]*c for _ in range(r)]
ds = [1, 0, -1, 0]
de = [0, 1, 0, -1]
js = je = 0
fs = fe = 0
fr, jh = deque(), deque()
for i in range(r):
    for j in range(c):
        if arr[i][j] == 'J':
            jihoon[i][j] = 1
            jh.append([i, j])
        elif arr[i][j] == 'F':
            fire[i][j] = 1
            fr.append([i, j])
print(bfs())