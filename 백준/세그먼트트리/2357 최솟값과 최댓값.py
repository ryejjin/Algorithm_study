import sys
input = sys.stdin.readline

# [1] 트리 생성
def init(arr, tree, node, start, end):
    mid = (start+end)//2
    if start == end:
        tree[node] = arr[node]
    else:
        init(arr, tree, node*2, start, mid)
        init(arr, tree, node*2+1, mid+1, end)
        tree[node] = tree[node*2]+tree[node*2+1]


n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
tree = [0] * (4*n)
init(arr, tree, 1, 0, n-1)
for _ in range(m):
    a, b = map(int, input().split())
