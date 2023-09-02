n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
INF = int(1e8)
# 최소 갯수를 구해야하기 때문에 dp테이블을 가장 큰 값으로 세팅
# 합이 idx가 되는 동전의 최소갯수를 dp에 저장
dp = [INF] * (k+1)
# dp[0]은 0으로 세팅
dp[0] = 0

for i in arr:
    for j in range(1, k+1):
        if j-i >= 0:
            # dp[j] = 그 전값, dp[j-i]는 i를 뺀 상태에서 동전의 최소갯수/ +1은 i의 가치를 가지는 동전을 사용하는 가짓수
            dp[j] = min(dp[j], dp[j-i]+1)

if dp[k] != INF:
    print(dp[k])
else:
    print(-1)