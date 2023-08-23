n = int(input())
arr = [0]+list(map(int, input().split()))
# 카드를 한장씩 더 살때마다 최댓값을 저장
dp = [0]*(n+1)
dp[1] = arr[1]

for i in range(2, n+1):
    temp_max = 0
    for j in range(i+1):
        temp = dp[j]+arr[i-j]
        if temp > temp_max:
            temp_max = temp
    dp[i] = temp_max

print(dp[-1])