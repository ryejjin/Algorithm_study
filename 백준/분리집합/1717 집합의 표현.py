import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find_parent(parent, k):
    if parent[k] != k:
        parent[k] = find_parent(parent, parent[k])
    return parent[k]
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a <= b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(m):
    x, a, b = map(int, input().split())
    if x == 0:
        union_parent(parent, a, b)

    elif x == 1:
        ax = find_parent(parent, a)
        bx = find_parent(parent, b)
        if ax == bx:
            print('YES')
        else:
            print('NO')