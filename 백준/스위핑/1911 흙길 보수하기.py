import sys
input = sys.stdin.readline

def bridge(x):
    global res, now
    temp = info[x][1] - info[x][0]
    if temp%l > 0:
        res += temp//l+1
        now += (temp//l + 1)*l
    else:
        res += temp//l
        now = info[x][1]

n, l = map(int, input().split())
info = []
for _ in range(n):
    s, e = map(int, input().split())
    info.append([s, e])

info.sort(key=lambda x: x[0])
res = 0
now = info[0][0]

for i in range(0, n):
    if now >= info[i][0]:
        info[i][0] = now
        bridge(i)
    else:
        now = info[i][0]
        bridge(i)

print(res)