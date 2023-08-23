def find_set(x):
    while x!= rep[x]:
        x = rep[x]
    return x

def union(x, y):
    rep[find_set(y)] = find_set(x)

V = int(input())
E = int(input())
rep = [i for i in range(V+1)]
graph = []
for _ in range(E):
    a, b, c = map(int, input().split())
    graph.append([a, b, c])

graph.sort(key=lambda x : x[2])

N = V+1
s = 0
cnt = 0
MST = []

for u, v, w in graph:
    if find_set(u) != find_set(v):
        cnt += 1
        s += w
        MST.append([u, v, w])
        union(u, v)
        if cnt == N-1:
            break
print(s)
