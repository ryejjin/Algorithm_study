n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.sort(key=lambda x:-x)

res = 0
for coin in coins:
    if k // coin > 0:
        res += (k//coin)
        k -= (k//coin)*coin

print(res)