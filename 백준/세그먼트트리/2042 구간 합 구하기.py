import sys
input = sys.stdin.readline

# [1] 트리 생성
def init(a, tree, node, start, end):
    if start == end:
        tree[node] = a[start]
    else:
        init(a, tree, node*2, start, (start+end)//2)
        init(a, tree, node*2+1, (start+end)//2+1, end)
        tree[node] = tree[node*2]+tree[node*2+1]

# [2] 변경된 값 업데이트
def update(a, tree, node, start, end, index, val):
    if index < start or index > end:
        return
    if start == end:
        a[index] = val
        tree[node] = val
        return
    update(a, tree, node*2, start, (start+end)//2, index, val)
    update(a, tree, node*2+1, (start+end)//2+1, end, index, val)
    tree[node] = tree[node*2]+tree[node*2+1]

# [3] 범위 찾은 후 구간 합 저장
def query(tree, node, start, end, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    lsum = query(tree, node*2, start, (start+end)//2, left, right)
    rsum = query(tree, node*2+1, (start+end)//2+1, end, left, right)
    return lsum+rsum


n, m, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
tree = [0] * (4*n)
m+=k
init(arr, tree, 1, 0, n-1)
for _ in range(m):
    a, b, c = map(int, input().split())
    if a == 1:
        update(arr, tree, 1, 0, n-1, b-1, c)
    else:
        print(query(tree, 1, 0, n-1, b-1, c-1))