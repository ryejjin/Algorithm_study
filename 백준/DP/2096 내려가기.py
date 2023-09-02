## 메모리 초과
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# arr = [list(map(int, input().split())) for _ in range(n)]
#
# memo_max = [[0]*3 for _ in range(n)]
# memo_min = [[0]*3 for _ in range(n)]
#
# if n == 1:
#     print(max(arr[-1]), min(arr[-1]))
#
# else:
#     for j in range(3):
#         memo_max[0][j] = arr[0][j]
#         memo_min[0][j] = arr[0][j]
#
#     for i in range(1, n):
#         memo_max[i][0] = max(memo_max[i-1][0], memo_max[i-1][1]) + arr[i][0]
#         memo_max[i][1] = max(memo_max[i-1][0], memo_max[i-1][1], memo_max[i-1][2]) + arr[i][1]
#         memo_max[i][2] = max(memo_max[i-1][1], memo_max[i-1][2]) + arr[i][2]
#
#
#         memo_min[i][0] = min(memo_min[i-1][0], memo_min[i-1][1]) + arr[i][0]
#         memo_min[i][1] = min(memo_min[i-1][0], memo_min[i-1][1], memo_min[i-1][2]) + arr[i][1]
#         memo_min[i][2] = min(memo_min[i-1][1], memo_min[i-1][2]) + arr[i][2]
#
#     print(max(memo_max[-1]), min(memo_min[-1]))

## retry

import sys
input = sys.stdin.readline

n = int(input())

dp_max = [0]*3
dp_min = [0]*3

temp_max = [0]*3
temp_min = [0]*3

for i in range(n):
    a, b, c = map(int, input().split())
    for j in range(3):
        if j == 0:
            temp_max[j] = a + max(dp_max[j], dp_max[j+1])
            temp_min[j] = a + min(dp_min[j], dp_min[j+1])
        elif j == 1:
            temp_max[j] = b + max(dp_max[j-1], dp_max[j], dp_max[j+1])
            temp_min[j] = b + min(dp_min[j-1], dp_min[j], dp_min[j+1])
        else:
            temp_max[j] = c + max(dp_max[j], dp_max[j-1])
            temp_min[j] = c + min(dp_min[j], dp_min[j-1])

    for k in range(3):
        dp_max[k] = temp_max[k]
        dp_min[k] = temp_min[k]

print(max(dp_max), min(dp_min))