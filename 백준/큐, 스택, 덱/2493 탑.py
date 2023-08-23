# 시간초과 (이름만 스택이지 리스트 순회와 다름없는듯?)
# import sys
# n = int(sys.stdin.readline())
# arr = list(map(int, sys.stdin.readline().split()))
# anw =[0]*n
# stack = []
# for i in range(n):
#     if len(stack) == 0:
#         stack.append(arr[i])
#     else:
#         stack.append(arr[i])
#         k = len(stack)
#         for j in range(k-2, -1, -1):
#             if stack[j] > arr[i]:
#                 anw[i] = j+1
#                 break

# print(*anw)

# 스택을 잘 활용하는 법
n = int(input())
top = list(map(int, input().split()))
stack = []
answer = [0 for i in range(n)]

for i in range(n):
    while stack:
        if stack[-1][1] > top[i]:
            answer[i] = stack[-1][0] + 1
            break
        else:
            stack.pop()
    stack.append([i, top[i]])

print(*answer)