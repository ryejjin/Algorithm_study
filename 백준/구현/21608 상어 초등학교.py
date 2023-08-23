import sys
input = sys.stdin.readline

n = int(input())

arr = [[0]*n for _ in range(n)]
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

temp = []
ans = 0     # 만족도
def find_seat(stu, a, b, c, d):
    near = []
    for i in range(n):
        for j in range(n):
            like = 0
            blank = 0
            for w in range(4):
                ni, nj = i+di[w], j+dj[w]
                if 0<=ni<n and 0<=nj<n:
                    if arr[ni][nj] == a or arr[ni][nj] == b or arr[ni][nj] == c or arr[ni][nj] == d:
                        like += 1
                    if arr[ni][nj] == 0:
                        blank += 1
            near.append((i, j, like, blank))
    near.sort(key=lambda x:(-x[2], -x[3], x[0], x[1]))
    for i in range(len(near)):
        x, y, li, bl = near[i]
        if arr[x][y] == 0:
            arr[x][y] = stu
            return

for _ in range(n*n):
    student, a, b, c, d = map(int, input().split())
    temp.append((student, a, b, c, d))
    find_seat(student, a, b, c, d)

for i in range(n*n):
    stu, a, b, c, d = temp[i]
    for j in range(n):
        for k in range(n):
            if arr[j][k] == stu:
                tmp = 0
                for w in range(4):
                    nj, nk = j+di[w], k+dj[w]
                    if 0<=nj<n and 0<=nk<n:
                        if arr[nj][nk] == a or arr[nj][nk] == b or arr[nj][nk] == c or arr[nj][nk] == d:
                            tmp += 1
                if tmp == 1:
                    ans += 1
                elif tmp == 2:
                    ans += 10
                elif tmp == 3:
                    ans += 100
                elif tmp == 4:
                    ans += 1000

print(ans)