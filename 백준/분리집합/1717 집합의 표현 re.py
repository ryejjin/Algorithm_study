import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
        return find_set(parent[x])
    return x

def union(x, y):
    if find_set(x) != find_set(y):
        parent[find_set(x)] = y

for _ in range(m):
    x, a, b = map(int, input().split())
    if x == 0:
        union(a, b)

    elif x == 1:
        if find_set(a) == find_set(b):
            print('YES')
        else:
            print('NO')