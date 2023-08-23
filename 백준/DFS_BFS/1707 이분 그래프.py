import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def dfs(k, color):
    global answer
    stack = [k]

    while stack:
        q = stack.pop()
        visit[q] = color
        for w in graph[q]:
            if visit[w] == 0:
                dfs(w, -color)
            elif visit[w] == visit[q]:
                answer = 'NO'
                return

for tc in range(int(input())):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    visit = [0] *(v+1)
    answer = 'YES'
    color = 1

    for i in range(1, v+1):
        if visit[i] == 0:
            dfs(i, color)
            if answer == 'NO':
                break
    print(answer)