def dfs(matrix, i, visited):
    stack = [i]
    visited[i] = True
    while stack:
        v = stack.pop()
        for j in matrix[v]:
            if not visited[j]:
                stack.append(j)
                visited[j] = True
                anw[j] = v

n = int(input())
matrix = [[]*(n+1) for _ in range(n+1)]
anw = [0] * (n+1)
visited = [False] * (n+1)
for _ in range(n-1):
    p, c = map(int, input().split())
    matrix[p].append(c)
    matrix[c].append(p)

dfs(matrix, 1, visited)

for i in range(2, n+1):
    print(anw[i])