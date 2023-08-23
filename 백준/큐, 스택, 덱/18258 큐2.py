from collections import deque
import sys
que = deque()

def push(a):
    return que.append(a)

def pop():
    return que.popleft()

def size():
    return len(que)

def empty():
    return len(que)

def front():
    return que[0]

def back():
    return que[-1]

n = int(sys.stdin.readline())
for _ in range(n):
    q = list(map(str, sys.stdin.readline().split()))
    
    if q[0] == 'push':
        push(q[1])
    if q[0] == 'pop':
        if len(que) == 0 : print(-1)
        else : print(pop())
    if q[0] == 'size':
        print(size())
    if q[0] == 'empty':
        if empty() == 0:
            print(1)
        else: print(0)
    if q[0] == 'front':
        if len(que) == 0 : print(-1)
        else : print(front())
    if q[0] == 'back':
        if len(que) == 0 : print(-1)
        else : print(back())