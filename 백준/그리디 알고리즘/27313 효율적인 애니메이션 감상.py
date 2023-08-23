def Time(x):
    if x < k:
        return arr[x]
    else:
        return memo[x-k]+arr[x]

n, m, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

memo = []

for i in range(n):
    time = Time(i)
    if time > m:
        break
    else:
        memo.append(time)

print(len(memo))