h, w = map(int, input().split())
arr = [input() for _ in range(h)]
anw = [[-1]*w for _ in range(h)]
for i in range(h):
    for j in range(0, w):
        cloud = 0
        if arr[i][j] == 'c':
            anw[i][j] = cloud
            for k in range(j+1, w):
                if arr[i][k] != 'c':
                    cloud += 1
                    anw[i][k] = cloud
                else:
                    break
for l in anw:
    print(*l)