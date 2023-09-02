s1 = list(input())
s2 = list(input())
N = len(s1)
M = len(s2)

dp = [0] * 1001

for i in range(N):
    temp = 0
    for j in range(M):
        if temp < dp[j]:
            temp = dp[j]
        elif s1[i] == s2[j]:
            dp[j] = temp+1
print(max(dp))