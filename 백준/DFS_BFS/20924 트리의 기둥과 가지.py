import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)


def giga(x, wt):
    global giga_node
    leaf = len(tree[x])
    if leaf < 3:
        giga_node += 1
        for k, w in tree[x]:
            if visit[k] == 0:
                visit[k] += wt+w
                giga(k, w+wt)

def branch(x, wt):
    for k, w in tree[x]:
        if visit_branch[k] == 0:
            visit_branch[k] += wt + w
            branch(k, w + wt)


# n : 노드의 개수, r : 루트노드의 번호
n, r = map(int, input().split())
tree = [[] for _ in range(n+1)]
visit = [0]*(n+1)
visit_branch = [0] * (n+1)
for _ in range(n-1):
    s, e, w = map(int, input().split())
    tree[s].append([e,w])
    tree[e].append([s,w])
giga_node = 0
giga(r, 0)
branch(giga_node, 0)

print(visit)
print(visit_branch)
print(max(visit), max(visit_branch))