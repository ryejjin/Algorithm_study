import sys; input=sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
memo = [0]*n

for i in range(n):
    cnt = 0
    for j in range(n):
        if cnt == arr[i] and memo[j] == 0:
            memo[j] = i+1
            break
        elif memo[j]==0:
            cnt += 1
print(*memo)