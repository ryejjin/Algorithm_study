import sys
input = sys.stdin.readline

def find_set(x):
    if friend[x] < 0:
        return x
    friend[x] = find_set(friend[x])
    return friend[x]

def union(p, q):
    p = find_set(p)
    q = find_set(q)
    if p == q:
        return
    friend[q] = p

def find_friend(i):
    for f in versus[i]:
        for w in versus[f]:
            union(i, w)

n = int(input())
m = int(input())
friend = [-1 for _ in range(n+1)]
versus = [[] for _ in range(n+1)]
for _ in range(m):
    r, P, Q = map(str, input().split())
    p, q = int(P), int(Q)
    if r == 'F':
        union(p, q)
    else:
        versus[p].append(q)
        versus[q].append(p)

for i in range(1, n+1):
    find_friend(i)
ans = 0
for i in range(1, n+1):
    if friend[i] == -1:
        ans += 1

print(ans)