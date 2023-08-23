import sys
input = sys.stdin.readline

flag = 1
while flag:
    arr = list(map(int, input().split()))
    if arr[0]==0:
        flag = 0
        break
    else:
        n = arr[0]
        arr = arr[1:]+[0]
        stack = [(0, arr[0])]
        res = 0

        for now in range(1, n+1):
            left = now
            while stack and stack[-1][1] > arr[now]:
                left, temp = stack.pop()
                res = max(res, temp*(now-left))
            stack.append((left, arr[now]))
        print(res)