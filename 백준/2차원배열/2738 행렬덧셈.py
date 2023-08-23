n, m = map(int, input().split())
ls_1 = [list(map(int, input().split())) for _ in range(n)]
ls_2 = [list(map(int, input().split())) for _ in range(n)]
ls_anw = [[0]*m for _ in range(n)]

for i in range(n):
    for j in range(m):
        ls_anw[i][j] = int(ls_1[i][j] + ls_2[i][j])

for i in ls_anw :
    for j in i:
        print(j,end=" ")
    print()