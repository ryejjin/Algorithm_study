arr = [list(input()) for _ in range(8)]
cnt = 0
for i in range(8):
    if i%2:
        for j in range(1, 9, 2):
            if arr[i][j] == 'F':
                cnt += 1
    else:
        for k in range(0, 8, 2):
            if arr[i][k] == 'F':
                cnt += 1

print(cnt)