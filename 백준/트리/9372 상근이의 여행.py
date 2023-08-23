# 중위 순회?
def inorder(v):
    global cnt
    if v != 0:
        inorder(tree[v][0])
        print(v, end=' ')
        cnt += 1
        inorder(tree[v][1])
    return cnt

t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    tree = [[0]*3 for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        if tree[a][0] == 0:
            tree[a][0] = b
        else:
            tree[a][1] = b
        tree[b][2] = a
    cnt = 0
    inorder(0)
    print(cnt)

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
    print(N - 1)