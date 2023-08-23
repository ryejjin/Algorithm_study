import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0
_sum = [0]*n

for i in range(n):
    _sum[i] = _sum[i-1]+arr[i]
    if _sum[i] == m:
        cnt += 1

for i in range(n-1, -1, -1):
    for j in range(i-1, -1, -1):
        if _sum[i]-_sum[j] == m:
            cnt += 1
            break

print(cnt)