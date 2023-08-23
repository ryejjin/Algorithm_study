# # 시간초과
# n, m = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]
# for _ in range(m):
#     x1, y1, x2, y2 = map(int, input().split())
#     _sum = 0
#     for i in range(x1-1, x2):
#         for j in range(y1-1, y2):
#             _sum += arr[i][j]
#     print(_sum)