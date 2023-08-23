import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(x):
    v[x] = True
    anw.append(x)
    for w in tree[x]:
        if not v[w]:
            dfs(w)

n = int(input())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    s, e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

chk = list(map(int, input().split()))
for k in range(n+1):
    tree[k].sort(key=lambda x: chk.index(x))
anw = []
v = [False]*(n+1)
dfs(1)

if chk == anw:
    print(1)
else:
    print(0)