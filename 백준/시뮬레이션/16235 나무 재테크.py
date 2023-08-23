import sys
input = sys.stdin.readline
from collections import deque

n, m, K = map(int, input().split())
nutrient = [[5]*n for _ in range(n)]
new_nutrient = [list(map(int, input().split())) for _ in range(n)]
soil = [[deque() for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x, y, z = map(int, input().split())
    soil[x-1][y-1].append(z)

di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]

new_seaseon = 0
while new_seaseon < K:
    season = 1
    # 봄
    summer = []
    for i in range(n):
        for j in range(n):
            tree = deque()
            next_n = 0
            for k in soil[i][j]:
                if nutrient[i][j] >= k:
                    nutrient[i][j] -= k
                    tree.append(k+1)
                else:
                    next_n += (k//2)
            nutrient[i][j] += next_n
            soil[i][j] = tree

    season += 2
    # 가을
    for i in range(n):
        for j in range(n):
            if soil[i][j]:
                for k in range(len(soil[i][j])):
                    if soil[i][j][k] % 5 == 0:
                        for w in range(8):
                            ni, nj = i+di[w], j+dj[w]
                            if 0<=ni<n and 0<=nj<n:
                                soil[ni][nj].appendleft(1)

    season += 1
    # 겨울
    for i in range(n):
        for j in range(n):
            nutrient[i][j] += new_nutrient[i][j]

    if season%4==0:
        new_seaseon+=1

ans = 0
for i in range(n):
    for j in range(n):
        ans += len(soil[i][j])
print(ans)