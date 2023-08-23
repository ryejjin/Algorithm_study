import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

arr = []
_min = int(1e9)
def delivery(num, cnt):
    global _min

    if num > len(chicken):
        return

    if cnt == k:
       res = 0
       for hx, hy in home:
           temp = int(1e9)
           for idx in arr:
               cx, cy = chicken[idx]
               temp = min(temp, abs(hx-cx)+abs(hy-cy))
           res += temp
       _min = min(_min, res)
       return
    arr.append(num)
    delivery(num+1, cnt+1)
    arr.pop()
    delivery(num+1, cnt)
    return _min

n, k = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(n)]
home = []
chicken = []

# 집과 치킨집의 좌표를 각각 저장
for i in range(n):
    for j in range(n):
        if info[i][j] == 1:
            home.append((i, j))
        elif info[i][j] == 2:
            chicken.append((i, j))


print(delivery(0, 0))