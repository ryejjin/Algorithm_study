# import sys
# input = sys.stdin.readline
# def perm(i, k):
#     global res
#     if i == k:
#         temp = [0]*n
#         temp[0] = order[0]
#         for x in range(1, n):
#             temp[x] = order[x]+temp[x-1]
#             if temp[x] > res:
#                 return
#         if res > sum(temp):
#             res = sum(temp)
#     else:
#         for j in range(k):
#             if visit[j] == 0:
#                 order[i] = arr[j]
#                 visit[j] = 1
#                 perm(i+1, k)
#                 visit[j] = 0
#
# n = int(input())
# arr = list(map(int, input().split()))
# order = [0]*n
# visit = [0]*n
# res = int(1e9)
# perm(0, n)
#
# print(res)


import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

res = 0

for i in range(N):
    for j in range(0, N-i):
        res += arr[j]
print(res)
