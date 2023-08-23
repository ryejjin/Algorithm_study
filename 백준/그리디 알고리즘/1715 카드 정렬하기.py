import heapq

n = int(input())
if n == 1:
    print(0)
else:
    q = []
    for _ in range(n):
        heapq.heappush(q, int(input()))

    res = 0
    while q:
        x = heapq.heappop(q)
        y = heapq.heappop(q)
        res += (x+y)
        if len(q) == 0:
            break
        heapq.heappush(q, x+y)

    print(res)