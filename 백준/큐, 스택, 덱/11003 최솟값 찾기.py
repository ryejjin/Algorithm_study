import sys
input = sys.stdin.readline
from collections import deque

n, l = map(int, input().split())
arr = list(map(int, input().split()))

q = deque()

for i in range(n):
    tmp = arr[i]

    while q and q[-1][1] > tmp:
        q.pop()

    q.append([i, tmp])

    if q[0][0] < i-l+1:
        q.popleft()

    print(q[0][1], end = ' ')