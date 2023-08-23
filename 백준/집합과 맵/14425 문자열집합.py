n, m = map(int, input().split())
strs = []
chks = []
for _ in range(n) :
    a = input()
    strs.append(a)
for _ in range(m) :
    b = input()
    chks.append(b)

cnt = 0
for chk in chks :
    if chk in strs :
        cnt += 1

print(cnt)