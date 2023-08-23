import sys, heapq
input = sys.stdin.readline

def problem(x):
    global ans
    q = []
    heapq.heappush(q, x)
    while q:
        t = heapq.heappop(q)
        ans.append(t)
        for w in lst[t]:
            degree[w] -= 1
            if degree[w] ==0:
                heapq.heappush(q, w)

n, m = map(int, input().split())
lst = [[] for _ in range(n+1)]
degree = [0] * (n+1)
ans = []
for _ in range(m):
    s, e = map(int, input().split())
    lst[s].append(e)
    degree[e] += 1

for j in range(1, n+1):
    if degree[j] == 0 and j not in ans:
        problem(j)

print(*ans)