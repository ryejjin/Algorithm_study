import sys
input = sys.stdin.readline

def perm(n, k):
    global _min
    if n == k:
        _sum = 0
        for x in range(N):
            if arr[order[x]][order[x+1]] != 0:
                _sum += arr[order[x]][order[x+1]]
                if _sum > _min:
                    return
            else:
                return
        if _min > _sum:
            _min = _sum
    else:
        for i in range(n):
            if visit[i] == 0:
                visit[i]=1
                order[k] = i
                perm(n, k+1)
                visit[i]=0

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

_min = int(1e9)
for j in range(N):
    visit = [0]*N
    order = [0]*(N+1)
    order[0] = order[N] = j
    visit[j] = 1
    perm(N, 1)

print(_min)