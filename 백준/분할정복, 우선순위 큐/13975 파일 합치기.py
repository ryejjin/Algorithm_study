import sys, heapq
input = sys.stdin.readline

t = int(input())
for tc in range(t):
    k = int(input())
    arr = list(map(int, input().split()))

    q = []
    for i in range(k):
        heapq.heappush(q, arr[i])

    res = 0

    while q:
        x = heapq.heappop(q)
        y = heapq.heappop(q)
        res += (x+y)
        if len(q)==0:
            break
        heapq.heappush(q, x+y)

    print(res)