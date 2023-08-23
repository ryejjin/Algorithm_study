from collections import deque

s = list(input())
a = deque()
b = deque()
cnt = 0

for i in range(len(s)):
    if s[i] == 'A':
        a.append(i)
    elif s[i] == 'B':
        b.append(i)
    elif s[i] == 'C':
        if len(b) > 0:
            b.popleft()
            cnt += 1

while a and b:
    pa = a.popleft()
    pb = b.popleft()
    if pa < pb:
        cnt += 1
    else:
        a.appendleft(pa)

print(cnt)