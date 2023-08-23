x, y = map(int,input().split())
idx_x = [0, x]
idx_y = [0, y]
n = int(input())
for _ in range(n):
    xy, num = map(int, input().split())
    if xy == 1:
        idx_x.append(num)
    else:
        idx_y.append(num)
idx_x.sort()
idx_y.sort()

max_square = 0
for i in range(1, len(idx_x)):
    for j in range(1, len(idx_y)):
        width = idx_x[i] - idx_x[i-1]
        height = idx_y[j] - idx_y[j-1]
        max_square = max(max_square, width * height)

print(max_square)