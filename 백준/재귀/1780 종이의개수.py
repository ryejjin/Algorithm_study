## 분할정복, 재귀

def dfs(x, y, n):
    global minus, zero, plus

    num = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != num:
                for k in range(3):
                    for l in range(3):
                        dfs(x+k*n//3, y+l*n//3, n//3)
                return
    if num == -1:
        minus += 1
    elif num == 0:
        zero += 1
    elif num == +1:
        plus += 1

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
minus = zero = plus = 0

dfs(0,0,n)
print(minus)
print(zero)
print(plus)
