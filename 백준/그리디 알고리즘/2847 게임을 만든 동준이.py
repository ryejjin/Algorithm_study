n = int(input())
arr = [int(input()) for _ in range(n)]

_max = arr[-1]-1
res = 0

for i in range(n-2, -1, -1):
    if arr[i] < _max :
        _max = arr[i]-1
    else:
        temp = arr[i]-_max
        res += temp
        _max -= 1

print(res)