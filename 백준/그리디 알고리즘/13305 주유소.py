n = int(input())
length = list(map(int, input().split()))
oil_price = list(map(int, input().split()))

min_price = oil_price[0]
total_price = 0
for i in range(n-1):
    min_price = min(min_price, oil_price[i])
    total_price += min_price*length[i]

print(total_price)