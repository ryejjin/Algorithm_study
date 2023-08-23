from collections import deque
import sys
input = sys.stdin.readline

def order(x):
    q = deque([x])
    time[x] += arr[x]
    while q:
        t = q.popleft()
        ans.append(t)
        for w in graph[t]:
            degree[w] -= 1
            time[w] = max(time[w], time[t]+arr[w])
            if degree[w] == 0:
                q.append(w)

t = int(input())
for tc in range(t):
    n, k = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    degree = [0] *(n+1)
    arr = [0] + list(map(int, input().split()))
    time = [0]*(n+1)
    ans = []

    for _ in range(k):
        s, e = map(int, input().split())
        graph[s].append(e)
        degree[e] += 1

    w = int(input())

    for i in range(1, n+1):
        if degree[i] == 0 and i not in ans:
            order(i)
    print(time[w])