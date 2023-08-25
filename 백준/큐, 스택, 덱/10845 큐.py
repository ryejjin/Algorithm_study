import sys
input = sys.stdin.readline
from collections import deque

q = deque()

n = int(input())
for _ in range(n):
    orders = list(input().split())
    order = orders[0]
    number = orders[-1]
    if order == 'push':
        q.append(int(number))
    elif order == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif order == 'size':
        print(len(q))
    elif order == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif order == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif order == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)