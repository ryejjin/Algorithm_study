import sys
input = sys.stdin.readline

def simulation(robot, direction, order):
    global result
    for i in range(b):
        for j in range(a):
            if arr[i][j][0] == robot:
                if direction == 'F':
                    ri, rj = dir[arr[i][j][1]]
                    cnt = 0
                    for k in range(1, order + 1):
                        ni, nj = i + ri * k, j + rj * k
                        if 0 <= ni < b and 0 <= nj < a:
                            cnt += 1
                            if arr[ni][nj] != [0, '']:
                                result = f'Robot {robot} crashes into robot {arr[ni][nj][0]}'
                                return
                            if cnt == order:
                                arr[ni][nj] = [robot, arr[i][j][1]]
                                arr[i][j] = [0, '']
                                return
                        else:
                            result = f'Robot {robot} crashes into the wall'
                            return

                if direction == 'R':
                    idx = NESW.index(arr[i][j][1])
                    n_idx = (idx + order) % 4
                    arr[i][j] = [robot, NESW[n_idx]]
                    return

                if direction == 'L':
                    idx = NESW2.index(arr[i][j][1])
                    n_idx = (idx+order) % 4
                    arr[i][j] = [robot, NESW2[n_idx]]
                    return

dir = {'N' : (-1, 0), 'E' : (0, 1), 'S':(1, 0), 'W':(0, -1)}
NESW = ['N', 'E', 'S', 'W']
NESW2 = ['N', 'W', 'S', 'E']

a, b = map(int, input().split())
n, m = map(int, input().split())
arr = [[[0, '']]*a for _ in range(b)]

for z in range(1, n+1):
    x, y, d = input().split()
    x, y = int(x), int(y)
    arr[b-y][x-1] = [z, d]
result = 'OK'

for _ in range(m):
    robot, direction, order = input().split()
    robot, order = int(robot), int(order)
    simulation(robot, direction, order)
    if result != 'OK':
        break

print(result)