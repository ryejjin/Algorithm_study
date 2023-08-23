L = int(input())
arr = [0] * (L+1)
n = int(input())
chk = []
for i in range(1, n+1):
    p, k = map(int, input().split())
    chk.append(k-p+1)
    for j in range(p, k+1):
        if arr[j]== 0:
            arr[j] = i

anw = []
for k in range(1, n+1):
    anw.append(arr.count(k))

_max = 0
_min = 1000
anw_max = anw_min = 0
for j in range(len(anw)):
    if anw[j] > _max:
        _max = anw[j]
        anw_max = j+1
a = max(chk)
idx = chk.index(a)+1
print(idx)
print(anw_max)