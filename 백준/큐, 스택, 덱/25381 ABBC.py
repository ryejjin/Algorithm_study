from collections import deque

s = list(input())
a = deque()
b = deque()
c = deque()
cnt = 0

for i in range(len(s)):
    if s[i] == 'A':
        a.append(i+1)
    elif s[i] == 'B':
        b.append(i+1)
    elif s[i] == 'C':
        c.append(i+1)

while a and b:
    ca = a.pop()
    cb = b.pop()
    if ca < cb:
        cnt += 1
    else:
        b.append(cb)

while c:
    cc = c.pop()
    for i in range(len(b)-1, -1, -1):
        if b[i] < cc:
            cnt += 1
            b.remove(b[i])
            break

print(cnt)