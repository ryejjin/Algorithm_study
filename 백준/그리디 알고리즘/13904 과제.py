n = int(input())
arr = []
for _ in range(n):
    d, w = map(int, input().split())
    arr.append((d, w))
arr.sort()
work = []
res = 0

for k in range(n, 0, -1):
    while arr and arr[-1][0] >= k:
        work.append(arr.pop()[1])
    if work:
        work.sort()
        res += work.pop()

print(res)