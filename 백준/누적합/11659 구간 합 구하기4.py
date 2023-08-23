# import sys
# n, m = map(int, sys.stdin.readline().split())
# num = list(map(int, sys.stdin.readline().split()))

# for _ in range(m):
#     i, j = map(int, sys.stdin.readline().split())
#     _sum = 0
#     for k in range(i-1, j):
#         _sum += num[k]
#     print(_sum)


import sys
n, m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

num_sum = [0]
for k in range(n):
    num_sum.append(num_sum[-1] + num[k]) 

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(num_sum[j] - num_sum[i-1])
    