import sys
input = sys.stdin.readline

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

N, M, K = map(int, input().split())
arr = [[[]for _ in range(N)]for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    arr[r-1][c-1].append([m, s, d])

for _ in range(K):
    # 불 이동
    fire = [[[] for _ in range(N)]for _ in range(N)]
    for i in range(N):
        for j in range(N):
            len_arr = len(arr[i][j])
            if len_arr > 0:
                for k in range(len_arr):
                    m, s, d = arr[i][j][k]
                    ni, nj = (i+di[d]*s)%N, (j+dj[d]*s)%N
                    fire[ni][nj].append([m,s,d])
    arr = [[[] for _ in range(N)] for _ in range(N)]
    # 2개 이상의 파이어볼 찾기
    for i in range(N):
        for j in range(N):
            len_fire = len(fire[i][j])
            if len_fire >= 2:
                temp_mass = temp_speed = temp_odd = temp_even = 0
                for k in range(len_fire):
                    temp_mass += fire[i][j][k][0]
                    temp_speed += fire[i][j][k][1]
                    if fire[i][j][k][2] % 2 : temp_odd+=1
                    else: temp_even += 1
                mass = temp_mass//5
                speed = temp_speed//len_fire
                if mass > 0:
                    if temp_odd == 0 or temp_even == 0:
                        arr[i][j].append([mass, speed, 0])
                        arr[i][j].append([mass, speed, 2])
                        arr[i][j].append([mass, speed, 4])
                        arr[i][j].append([mass, speed, 6])
                    else:
                        arr[i][j].append([mass, speed, 1])
                        arr[i][j].append([mass, speed, 3])
                        arr[i][j].append([mass, speed, 5])
                        arr[i][j].append([mass, speed, 7])
            else:
                arr[i][j] = fire[i][j]

fire_mass = 0
for i in range(N):
    for j in range(N):
        _fire = len(arr[i][j])
        if _fire > 0:
            for k in range(_fire):
                fire_mass += arr[i][j][k][0]

print(fire_mass)