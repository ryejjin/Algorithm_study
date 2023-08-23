import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


def dfs(i):
    for k in range(n):
        if arr[i][k] == 1 and visit[k] == 0:
            visit[k] = 1
            dfs(k)

for i in range(n):
    visit = [0]*n
    dfs(i)
    for j in range(n):
        if visit[j] == 1:
            print(1, end = ' ')
        else:
            print(0, end = ' ')
    print()