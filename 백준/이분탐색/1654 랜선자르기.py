#매개변수탐색
import sys
input = sys.stdin.readline

k, n = map(int, input().split())
line = [int(input()) for _ in range(k)]
line.sort()

s, e = 1, max(line)
res = 0
while s <= e:
    mid = (s+e)//2
    cnt = 0
    for i in range(k):
        cnt += line[i]//mid

    if cnt >= n:
        s = mid+1
        res = mid
    else:
        e = mid-1

print(res)