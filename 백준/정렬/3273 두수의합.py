import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
arr.sort()

res = 0
s,e = 0, n-1

while s < e:
    ans = arr[s]+arr[e]

    if ans == x:
        res += 1
        s += 1
    elif ans < x:
        s += 1
    else:
        e -= 1

print(res)