import sys
input = sys.stdin.readline

def perm(i, k):
    global res
    if i == k:
        a = 500
        for w in range(n):
            a += order[w] - K
            if a < 500:
                return
        res += 1

    else:
        for j in range(k):
            if visit[j] == 0:
                order[i] = arr[j]
                visit[j] = 1
                perm(i+1, k)
                visit[j] = 0

n, K = map(int, input().split())
arr = list(map(int, input().split()))

order = [0]*n
visit = [0]*n

res = 0

perm(0, n)

print(res)