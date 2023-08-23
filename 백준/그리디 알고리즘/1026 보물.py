### 시간초과
# import sys
# input = sys.stdin.readline
#
# def perm(i, k):
#     global res
#     if i == k:
#         temp = 0
#         for k in range(n):
#             temp += order[k]*B[k]
#             if temp > res:
#                 return
#         if temp < res:
#             res = temp
#     else:
#         for j in range(k):
#             if visit[j] == 0:
#                 order[i] = A[j]
#                 visit[j] = 1
#                 perm(i+1, k)
#                 visit[j] = 0
#
# n = int(input())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
#
# res = int(1e9)
# order = [0]*n
# visit = [0]*n
# perm(0, n)
#
# print(res)

###
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort()
B.sort(reverse=True)
lsum = 0
for i in range(N):
    lsum += A[i] + B[i]
print(A)
print(B)
print(lsum)


# for i in range(N):
#     lsum = lsum + min(A) * max(B)
#     A.pop(A.index(min(A)))
#     B.pop(B.index(max(B)))
# print(lsum)