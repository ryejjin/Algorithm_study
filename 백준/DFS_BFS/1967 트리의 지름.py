# 루트노드에서 가장 거리가 먼 점 t를 잡은 후, 그 점에서 가장 먼 점 u를 찾으면 지름
# n이 1일때는 0이 출력되야한다. (visit를 -1로 잡는 이유)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

def dfs(x, wt):
    for e, w in tree[x]:
        if visit[e] == -1:
            visit[e] += wt+w+1      # visit를 -1로 잡았기 때문에 지름에 영향이 안가도록 +1도 같이 해줘야함.
            dfs(e, wt+w)


n = int(input())
tree = [[] for _ in range(n+1)]
visit = [-1]*(n+1)
for _ in range(n-1):
    s, e, w = map(int, input().split())
    tree[s].append([e, w])
    tree[e].append([s, w])

# 루트노드에서 가장 먼 점 t 찾기
visit[1] = 0
dfs(1, 0)
t = visit.index(max(visit))

# visit 초기화
visit = [-1]*(n+1)
visit[t] = 0
# t점에서 가장 먼 점 u까지의 거리
dfs(t,0)

print(max(visit))