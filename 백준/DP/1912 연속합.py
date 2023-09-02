import sys
input = sys.stdin.readline

INF = int(1e9)
n = int(input())
arr = [-INF] + list(map(int, input().split()))
dp = [0]*(n+1)
dp[0] = -INF
dp[1] = arr[1]
for i in range(2, n+1):
    dp[i] = max(dp[i-1]+arr[i], arr[i])
print(max(dp))
print(dp)





###시간초과
# INF = int(1e9)
# n = int(input())
# arr = [-INF]+list(map(int, input().split()))
# dp = [0]*(n+1)
# dp[0] = -INF
# dp[1] = max(arr)
# for i in range(2, n+1):
#     _max = -INF
#     for j in range(1, n+1-i):
#         temp = sum(arr[j:j+i])
#         if _max < temp:
#             _max = temp
#     dp[i] = _max
#
# print(max(dp))