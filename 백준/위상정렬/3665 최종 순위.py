import sys, heapq
input = sys.stdin.readline

def order(x):
    q = []
    heapq.heappush(q, x)
    while q:
        t = heapq.heappop(q)
        ans.append(t)
        for w in range(1, n+1):
            if degree[w] > 0:
                degree[w] -= 1
                if degree[w] == 0:
                    heapq.heappush(q, w)

t = int(input())
for tc in range(t):
    n = int(input())
    degree = [0]*(n+1)
    arr = list(map(int, input().split()))
    for i in range(n):
        degree[arr[i]] += i
    m = int(input())
    if m == 0:
        print(*arr)
    else:
        for _ in range(m):
            s, e = map(int, input().split())
            idx_s = arr.index(s)
            idx_e = arr.index(e)
            if idx_s > idx_e:
                degree[s] -= 1
                degree[e] += 1
            else:
                degree[s] += 1
                degree[e] -= 1
        # print(degree)
        ans = []
        for i in range(1, n+1):
            if degree[i] == 0:
                order(i)
                break

        if len(ans)==n:
            print(*ans)
        else:
            print('IMPOSSIBLE')

'''
1
5
1 4 3 5 2
7
1 2
1 3 
1 4
1 5
2 4 
3 4
4 5

ans : 3 5 2 4 1
'''