import sys
n = int(sys.stdin.readline())
arr = [[0] * 1001 for _ in range(1001)]
i = 1
for _ in range(n):
    x, y, s, e = map(int, sys.stdin.readline().split())
    for k in range(x, x+s):
        for l in range(y, y+e):
            arr[l][k] = i
    i += 1

for j in range(1, n+1):
    cnt = 0
    for r in range(1001):
        cnt += arr[r].count(j)
    print(cnt)


## 너무 느리다!
# anw = []
# paper = 1
# while paper < 102:
#     cnt = 0
#     for a in range(1001):
#         for b in range(1001):
#             if arr[a][b] == paper:
#                 cnt += 1
#     anw.append(cnt)
#     paper += 1
# anw = list(filter(None, anw))
# for j in range(len(anw)):
#     print(anw[j])