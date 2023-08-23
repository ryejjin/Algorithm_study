n = int(input())
weight = [int(input()) for _ in range(n)]
weight.sort()

res = 0
while weight:
    t = weight.pop(0)
    if res < n*t:
        res = n*t
        n -= 1
    else:
        n-=1

print(res)