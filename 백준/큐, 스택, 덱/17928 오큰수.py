n = int(input())
arr = list(map(int, input().split()))


ans = [-1]*n
stack = []

for i in range(n-1, -1, -1):
    temp = arr[i]

    while stack and stack[-1]<=temp:
        stack.pop()
    if stack:
        ans[i] = stack[-1]
    stack.append(temp)

print(*ans)