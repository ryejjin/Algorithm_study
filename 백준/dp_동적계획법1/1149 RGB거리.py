n = int(input())
ls = [list(map(int, input().split())) for _ in range(n)]

cost = [[0] * 3 for _ in range(n+1)]
for i in range(1,n+1):
    cost[i][0] = min(cost[i-1][1],cost[i-1][2]) + ls[i-1][0]
    cost[i][1] = min(cost[i-1][0],cost[i-1][2]) + ls[i-1][1]
    cost[i][2] = min(cost[i-1][1],cost[i-1][0]) + ls[i-1][2]

print(min(cost[n][0], cost[n][1], cost[n][2]))