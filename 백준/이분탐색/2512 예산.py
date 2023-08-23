n = int(input())
arr = sorted(list(map(int,input().split())))
m = int(input())

s = 1
e = arr[-1]
anw = 0
while s <= e:
    mid = (s+e)//2
    _sum = 0
    for i in range(n):
        if arr[i] >= mid:
            _sum += mid
        else:
            _sum += arr[i]

    if _sum > m :
        e = mid-1
    else:
        anw = mid
        s = mid+1

print(anw)