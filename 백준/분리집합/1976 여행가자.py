import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N = int(input())
M = int(input())
info = [[0]*(N+1)]+[[0]+list(map(int, input().split())) for _ in range(N)]
plan = list(map(int, input().split()))

parent = [i for i in range(N+1)]

# union연산 : 서로 연결된 두 노드 확인
for i in range(1, N+1):
    for j in range(1, N+1):
        if info[i][j] == 1:
            union_parent(parent, i, j)


for k in range(1, N+1):
    find_parent(parent, k)


start = parent[plan[0]]
for city in plan:
    if parent[city] != start:
        print('NO')
        exit()
print('YES')

