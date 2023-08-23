import sys
input = sys.stdin.readline

def dfs(x):
    visit[x] = 1
    stack = [x]

    while stack:
        k = stack.pop()
        for w in graph[k]:
            if visit[w] == 0:
                answer[w] += answer[k]
                visit[w] = 1


n, m = map(int, input().split())
arr = list(map(int, input().split()))
graph = [[] for _ in range(n+1)]
answer = [0]*(n+1)

for i in range(1, n):
    graph[arr[i]].append(i+1)

for _ in range(m):
    p, w = map(int, input().split())
    answer[p] += w

visit = [0] *(n+1)
for i in range(1, n+1):
    dfs(i)

for l in range(1, n+1):
    print(answer[l], end = ' ')