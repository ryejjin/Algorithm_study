import sys
input = sys.stdin.readline

n = int(input())
info = []
people = 0
for _ in range(n):
    x, a = map(int, input().split())
    info.append((x, a))
    people += a
info.sort(key=lambda x: x[0])

res = 0
for i in range(n):
    res += info[i][1]
    if res >= people/2:
        print(info[i][0])
        break