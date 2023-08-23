def tree(x, y, n):
    num = arr[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != num:        # n이 1인 경우(즉, 하나라도 다르면)
                print("(", end='')
                n = n // 2
                tree(x, y, n)  # 오른쪽 위
                tree(x, y + n, n)  # 왼쪽 위
                tree(x + n, y, n)  # 오른쪽 아래
                tree(x + n, y + n, n)  # 왼쪽 아래
                print(")", end='')
    # n이 2이상인 경우 위의 조건이 통과되기 때문에
    if num == 1:
        print(1, end='')
    else:
        print(0, end='')

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]

tree(0, 0, n)
