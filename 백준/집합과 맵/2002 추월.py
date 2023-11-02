import sys
input = sys.stdin.readline

n = int(input())
before = {}
after = [0]*n

for i in range(n):
    before[input()] = i
for i in range(n):
    after[i] = before[input()]

ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        if after[i] > after[j]:
            ans += 1
            break

print(before)
print(after)
print(ans)