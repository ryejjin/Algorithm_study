# [1] 배열 A를 이용해 세그먼트 트리 만들기
######
# a : 배열 A
# tree : 세그먼트 트리
# node : 노드 번호
# node에 저장되어 있는 합의 범위가 strat-end
def init(a, tree, node, start, end):
    mid = (start+end)//2
    # 리프 노드인 경우 >> 리프노드는 배열의 그 수를 저장해야하기 때문에 tree[node]=a[start]가 됨
    if start == end :
        tree[node] = a[start]
    else:
        # 노드의 왼쪽 자식
        init(a, tree, node*2, start, mid)
        # 노드의 오른쪽 자식
        init(a, tree, node*2+1, mid+1, end)
        tree[node] = tree[node*2] + tree[node*2+1]

# [2] [left, right]의 합 구하기
def query(tree, node, start, end, left, right):
    # [left, right]와 [start, end]가 겹치지 않는 경우
    if left > end or right < start :
        return 0
    # [left, right]가 [start, end]를 완전히 포함하는 경우
    if left <= start and end <= right:
        return tree[node]
    # [start, end]가 [left, right]를 완전히 포함하는 경우
    # OR [left, right]와 [start, end]가 겹쳐져 있는 경우 (앞선 경우를 제외한 나머지)
    # >> 왼쪽 자식과 오른쪽 자식을 루트로 하는 트리에서 다시 탐색을 시작해야 함
    mid  = (start+end)//2
    lsum = query(tree, node*2, start, mid, left, right)
    rsum = query(tree, node*2+1, mid+1, end, left, right)
    return lsum+rsum

# [3] 수 변경하기
# index번 째 수를 vale로 변경하는 경우, index번쨰를 포함하는 노드에 들어있는 합만 변경해주면 됨
# 원래 index번째 수가 a[index]였고, 바뀐 수가 val이라면, 합은 val-a[index]만큼 변함

# 아래의 함수에서 index번째를 포함하는 모든 노드의 합에 diff를 더해서 수를 변경하는 함수
def update_tree(tree, node, start, end, index, diff):
    if index < start or index > end:
        return
    tree[node] = tree[node] + diff
    if start != end:
        mid = (start+end)//2
        update_tree(tree, node*2, start, mid, index, diff)
        update_tree(tree, node*2+1, mid+1, end, index, diff)
# index번째를 val로 변경하는 코드
def update(a, tree, n, index, val):
    diff = val - a[index]
    a[index] = val
    update_tree(tree, 1, 0, n-1, index, diff)

# [3-1] 수 변경하기 2
# 리프 노드를 찾을때까지 재귀호출을 이어나가다가, 리프노드를 찾으면 그 노드의 합을 변경
# 이후 리턴 될때마다 각 노드의 합을 자식에 저장된 합을 이용해 다시 구하는 방법
def update2(a, tree, node, start, end, index, val):
    if index < start or index > end:
        return
    if start == end:
        a[index] = val
        tree[node] = val
        return
    mid = (start+end)//2
    update(a, tree, node*2, start, mid, index, val)
    update(a, tree, node*2+1, mid+1, end, index, val)
    tree[node] = tree[node*2] + tree[node*2+1]