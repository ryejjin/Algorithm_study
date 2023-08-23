def paper(x, y, n):
    global white, blue

    num = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != num:
                for k in range(2):
                    for l in range(2):
                        paper(x+k*n//2, y+l*n//2, n//2)
                return
    if num == 1:
        blue += 1
    elif num == 0:
        white += 1

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# white : 0, blue : 1
white = 0
blue = 0

paper(0, 0, n)
print(white)
print(blue)