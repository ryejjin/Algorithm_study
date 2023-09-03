import sys
input = sys.stdin.readline

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
know = list(map(int, input().split()))[1:]

parent = [i for i in range(n+1)]
for i in know:
    parent[i] = 0

parties = []
for _ in range(m):
    info = list(map(int, input().split()))
    p = info[0]
    party = info[1:]
    for i in range(p-1):
        union(party[i], party[i+1])
    parties.append(party)

ans = 0
for party in parties:
    known = False
    for i in range(len(party)):
        if find(party[i]) == 0:
            known = True
            break
    if not known:
        ans += 1

print(ans)