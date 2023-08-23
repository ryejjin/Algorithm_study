from collections import deque

N = int(input())

q = deque([])
for i in range(1, N+1):
    q.append(i)

while len(q) > 1:
    q.popleft()
    x = q.popleft()
    q.append(x)


print(q[0])