# 트리의 레벨 구하기
import sys
input = sys.stdin.readline
def lv(x, level):
    global max_level
    if max_level < level:
        max_level = level
    tree[x][4] = level
    c1, c2 = tree[x][0], tree[x][1]
    if c1 != 0:
        lv(c1, level+1)
    if c2 != 0:
        lv(c2, level+1)

# 중위순회한 순서가 해당 노드의 너비
def inorder(v):
    global width
    if v!=0:
        inorder(tree[v][0])
        tree[v][3] = width
        width += 1
        inorder(tree[v][1])

n = int(input())
tree = [[0]*5 for _ in range(n+1)]

for _ in range(n):
    p, l, r = map(int, input().split())
    if l != -1:
        tree[p][0] = l
        tree[l][2] = p
    if r != -1:
        tree[p][1] = r
        tree[r][2] = p
width = level = max_level = 1

# 루트노드 구하기
root = 0
for i in range(1, n+1):
    if tree[i][2] == 0:
        root = i

inorder(root)
lv(root, level)

chk = [[] for _ in range(max_level+1)]
for j in range(n+1):
    chk[tree[j][4]].append(tree[j][3])

ans = -10e6
ans_level = 0
result = []
for k in range(1, max_level+1):
    temp = max(chk[k]) - min(chk[k]) +1
    if ans < temp:
        ans = temp
        ans_level = k

print(ans_level, ans)