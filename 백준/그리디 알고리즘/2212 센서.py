n = int(input())
k = int(input())
sensor = sorted(list(map(int, input().split())))

if n <= k:
    print(0)
else:
    gap = []
    for i in range(n-1):
        gap.append(sensor[i+1]-sensor[i])

    gap.sort(reverse=True)

    for _ in range(k-1):
        gap.pop(0)

    print(sum(gap))