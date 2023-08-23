import sys
input = sys.stdin.readline

def turn(dir):
    up, down, left, right, front, back = dice[0], dice[5], dice[3], dice[2], dice[4], dice[1]

    if dir == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = right, back, down, up, front, left

    elif dir == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = left, back, up, down, front, right

    elif dir == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = front, up, right, left, down, back

    elif dir == 4:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = back, down, right, left, up, front

n, m, x, y, k = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(n)]
arr = list(map(int, input().split()))

dice = [0] * 6

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


for c in arr:
    x+=dx[c-1]; y+=dy[c-1]
    if 0 > x or x >= n or 0 > y or y >= m:
        x-=dx[c-1]; y-=dy[c-1]
        continue
    else:
        turn(c)
        if MAP[x][y] == 0:
            MAP[x][y] = dice[-1]
        else:
            dice[-1] = MAP[x][y]
            MAP[x][y] = 0
    print(dice[0])