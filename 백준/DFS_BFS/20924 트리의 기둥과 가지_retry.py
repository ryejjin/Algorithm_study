import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def giga(x, wt):
    global giga_node, flag
    if flag:
        leaf = len(tree[x])
        if leaf > 2:
            giga_node = x
            flag = 0
        else:
            giga_node += 1
            for k, w in tree[x]:
                if visit[k] == 0:
                    visit[k] += wt + w
                    giga(k, w + wt)
    for k, w in tree[x]:
        if visit[k] == 0:
            visit[k] += wt + w
            giga(k, w + wt)


# n : 노드의 개수, r : 루트노드의 번호
n, r = map(int, input().split())
tree = [[] for _ in range(n+1)]
visit = [0]*(n+1)
visit[r] = 1
flag = 1
giga_node = 1
for _ in range(n-1):
    s, e, w = map(int, input().split())
    tree[s].append([e,w])
    tree[e].append([s,w])
giga(r, 0)
visit[r]=0

if giga_node > n:
    giga_node -= 1

if giga_node == r:
    print(0, max(visit))
elif giga_node == 1:
    print(max(visit), 0)
else:
    print(visit[giga_node] - visit[r], max(visit) - visit[giga_node])

print(giga_node)
print(visit)
