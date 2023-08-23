# 맥주의 갯수는 중요하지 않음
# 최대 1000m까지 갈 수 있다.

from collections import deque

def bfs():
    q = deque([[hx, hy]])
    while q:
        i, j = q.popleft()
        if abs(i-fx) + abs(j-fy) <= 1000:
            print('happy')
            return
        for k in range(n):      # 편의점 순회
            if not v[k]:        # 편의점에 방문하지 않았다면
                x, y = store[k]     # 좌표 pop
                if abs(x-i) + abs(y-j) <= 1000:
                    q.append([x,y])
                    v[k] = 1
    print('sad')
    return

for tc in range(int(input())):
    n = int(input())
    hx, hy = map(int, input().split())
    store = [list(map(int, input().split())) for _ in range(n)]
    fx, fy = map(int, input().split())
    v = [0 for _ in range(n+1)]     # 편의점 방문 여부
    bfs()