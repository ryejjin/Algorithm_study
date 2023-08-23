n, m = map(int, input().split())
arr = list(map(int, input().split()))
minus = []
plus = []
dis = 0

for i in arr:
    if i < 0:
        minus.append(i)
    else:
        plus.append(i)
    if abs(i)>abs(dis):
        dis = i

minus.sort()
plus.sort(reverse=True)
ans = 0

for j in range(0, len(plus), m):
    if plus[j]!=dis:
       ans += plus[j]

for k in range(0, len(minus), m):
    if minus[k]!=dis:
        ans += abs(minus[k])

ans *= 2
ans += abs(dis)
print(ans)